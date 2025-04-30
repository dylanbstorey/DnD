import os
import angreal
from pathlib import Path
import glob
import re
from typing import Optional, List

import angreal
import os




# Create a command group named "new"
new = angreal.group(
    name="new",
    about="Create new D&D campaign components"
)

@new
@angreal.command(name="campaign", about="create a new campaig structure for development")
@angreal.argument(name="name", required=True, help="Name of the campaign")
def campaign(name: str):
    """
    Create a new D&D campaign with the required directory structure.
    
    This command will create a new campaign directory with the appropriate
    structure as defined in the repository guide.
    """
    # Convert campaign name to kebab-case
    campaign_dir = name.lower().replace(' ', '-')
    
    # Create main campaign directory
    campaign_path = Path(f"{campaign_dir}")
    campaign_path.mkdir(exist_ok=True)
    
    # Create README.md
    with open(f"{campaign_path}/README.md", "w") as f:
        f.write(f"# {name}\n\n")
        f.write(f"Campaign overview for {name}. Edit this file to provide a high-level description of your campaign.\n")
    
    # Create subdirectories
    subdirs = [
        "campaign/world",
        "campaign/world/maps",
        "campaign/lore",
        "characters/npcs/allies",
        "characters/npcs/villains",
        "modules/00-campaign-reference/monsters",
        "modules/00-campaign-reference/npcs",
        "modules/00-campaign-reference/mechanics",
        "modules/01-introduction",
        "sessions"
    ]
    
    for subdir in subdirs:
        Path(f"{campaign_path}/{subdir}").mkdir(parents=True, exist_ok=True)
    
    # Create initial files
    initial_files = {
        "campaign/overview.md": f"# {name} Overview\n\n## Campaign Premise\n\n[Describe your campaign premise here]\n\n## Theme and Tone\n\n[Describe the theme and tone of your campaign]\n\n## Major Story Arcs\n\n1. [First major arc]\n2. [Second major arc]\n3. [Third major arc]\n",
        "campaign/timeline.md": f"# {name} Timeline\n\n## Historical Events\n\n### [Ancient Era]\n- [Historical event 1]\n- [Historical event 2]\n\n### [Recent History]\n- [Recent event 1]\n- [Recent event 2]\n\n## Campaign Timeline\n\n### Pre-Campaign Events\n- [Event that happened before the campaign started]\n\n### Current Events\n- [Current event 1]\n\n## Future Events (DM Only)\n- [Planned event 1]\n- [Planned event 2]\n",
        "campaign/world/locations.md": f"# {name} Locations\n\n## Major Regions\n\n### [Region Name]\n**Description:** [Brief description]\n**Notable Features:** [List of features]\n**Settlements:** [List of settlements]\n\n## Important Settlements\n\n### [Settlement Name]\n**Population:** [Population size and composition]\n**Government:** [Government type]\n**Notable NPCs:** [List of important NPCs]\n**Points of Interest:** [List of locations within the settlement]\n",
        "campaign/world/factions.md": f"# {name} Factions\n\n## [Faction Name]\n**Alignment:** [Faction alignment]\n**Leader:** [Faction leader]\n**Headquarters:** [Faction base of operations]\n**Goals:** [Faction objectives]\n**Resources:** [Faction assets and capabilities]\n**Relationships:** [How this faction relates to others]\n",
        "characters/progression-tracker.md": f"# Character Progression Tracker\n\n## Current Party Status\n\n| Character | Player | Level | XP | Next Level | Notes |\n|-----------|--------|-------|----|-----------|---------|\n| [Character 1] | [Player 1] | [Level] | [Current XP] | [XP for next level] | [Notes] |\n| [Character 2] | [Player 2] | [Level] | [Current XP] | [XP for next level] | [Notes] |\n\n## Milestones\n\n| Milestone | Description | Characters Present | Rewards |\n|-----------|-------------|-------------------|--------|\n| [Milestone 1] | [Description] | [Characters] | [Rewards] |\n\n## Session Log\n\n| Session | Date | Summary | XP Awarded |\n|---------|------|---------|------------|\n| [Session 1] | [Date] | [Brief summary] | [XP] |\n",
        "modules/01-introduction/module.md": f"# Introduction to {name}\n\n## Adventure Summary\n\n[Provide a brief summary of this introductory adventure]\n\n## Adventure Hooks\n\n1. [Hook 1 - How players get involved]\n2. [Hook 2 - Alternative path into the adventure]\n\n## Key Locations\n\n### [Location 1]\n**Description:** [Description of the location]\n**Encounters:** [What happens here]\n**Treasure:** [What can be found]\n\n## Important NPCs\n\n### [NPC 1]\n**Role:** [NPC's role in the adventure]\n**Description:** [Physical description]\n**Personality:** [How they behave]\n**Motivation:** [What they want]\n\n## Encounters\n\n### [Encounter 1]\n**Type:** [Combat/Social/Puzzle/Trap]\n**Difficulty:** [Easy/Medium/Hard]\n**Description:** [What happens]\n**Creatures:** [Monsters or NPCs involved]\n**Treasure:** [Rewards for success]\n",
        "sessions/session-log.md": f"# {name} Session Log\n\n| # | Date | Summary | Key Events |\n|---|------|---------|------------|\n\n"
    }
    
    for file_path, content in initial_files.items():
        with open(f"{campaign_path}/{file_path}", "w") as f:
            f.write(content)
    
    print(f"Campaign '{name}' created successfully at {campaign_path}/")
    print("Directory structure has been set up with initial files.")
    print("Next steps:")
    print("1. Edit campaign/overview.md to establish your campaign premise")
    print("2. Create a basic timeline.md with major historical events")
    print("3. Populate initial world building files with key locations and factions")

def get_campaign_directories() -> List[str]:
    """Get a list of campaign directories in the current directory."""
    # Get all directories that have a campaign structure
    campaign_dirs = []
    
    # Check for directories that have the expected subdirectories
    for directory in glob.glob("*/"):
        directory = directory.rstrip('/')
        if os.path.isdir(f"{directory}/campaign") and os.path.isdir(f"{directory}/sessions"):
            campaign_dirs.append(directory)
    
    return campaign_dirs

def get_next_session_number(campaign: str) -> int:
    """Get the next session number for a campaign."""
    # Get all existing session directories
    session_dirs = glob.glob(f"{campaign}/sessions/session-*/")
    
    if not session_dirs:
        return 1
    
    # Extract session numbers from directory names
    session_numbers = []
    for session_dir in session_dirs:
        match = re.search(r'session-(\d+)', session_dir)
        if match:
            session_numbers.append(int(match.group(1)))
    
    # Return the next number
    return max(session_numbers) + 1 if session_numbers else 1

@new
@angreal.command(name="session", about="create a new campaig structure for development")
@angreal.argument(name ="campaign", long="campaign", help="The campaign to create a session for")
def session(campaign: Optional[str] = None):
    """
    Create a new session document for a D&D campaign.
    
    This command will create a new session directory and session document
    based on the session template.
    """
    # Get list of campaigns
    campaign_dirs = get_campaign_directories()
    
    if not campaign_dirs:
        print("No campaigns found. Please create a campaign first using 'angreal new campaign'.")
        return
    
    # If campaign not specified, prompt user to select
    if not campaign:
        print("Available campaigns:")
        for i, campaign_dir in enumerate(campaign_dirs, 1):
            print(f"{i}. {campaign_dir}")
        
        try:
            choice = int(input("Select a campaign (number): "))
            if 1 <= choice <= len(campaign_dirs):
                campaign = campaign_dirs[choice - 1]
            else:
                print("Invalid selection.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    elif campaign not in campaign_dirs:
        print(f"Campaign '{campaign}' not found.")
        return
    
    # Get next session number
    session_number = get_next_session_number(campaign)
    
    # Create session directory
    session_dir = f"{campaign}/sessions/session-{session_number:02d}"
    os.makedirs(session_dir, exist_ok=True)
    
    # Copy session template
    template_path = os.path.join(angreal.get_root(), "templates", "session.md")
    
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
    
    # Add session number to the content
    session_content = f"# Session {session_number}\n\n{template_content}"
    
    # Write session file
    session_file_path = f"{session_dir}/session-{session_number:02d}.md"
    with open(session_file_path, "w") as session_file:
        session_file.write(session_content)
    
    # Update session log
    session_log_path = f"{campaign}/sessions/session-log.md"
    with open(session_log_path, "r") as log_file:
        log_content = log_file.read()
    
    # Add new session entry to the log
    new_row = f"| {session_number} | [Date] | [Summary] | [Key Events] |\n"
    
    # Find the table in the log content and add the new row
    if "| # | Date | Summary | Key Events |" in log_content:
        log_content = log_content.replace("| # | Date | Summary | Key Events |\n|---|------|---------|------------|", 
                                         f"| # | Date | Summary | Key Events |\n|---|------|---------|------------|\n{new_row.rstrip()}")
    else:
        # If the table format is different or missing, just append the new row
        log_content = f"{log_content}\n{new_row}"
    
    with open(session_log_path, "w") as log_file:
        log_file.write(log_content)
    
    print(f"Session {session_number} created successfully at {session_file_path}")
    print(f"Session log updated at {session_log_path}")
    print("Next steps:")
    print("1. Fill out the session preparation sections")
    print("2. Update the session date")
    print("3. Add expected story beats and encounters")


@new
@angreal.command(name="module", about="create a new module for a campaign")
@angreal.argument(name="name", required=True, help="Name of the module")
@angreal.argument(name="campaign", long="campaign", help="The campaign to create a module for")
def module(name: str, campaign: Optional[str] = None):
    """
    Create a new adventure module for a D&D campaign.
    
    This command will create a new module directory and files
    with the appropriate structure for an adventure module.
    """
    # Get list of campaigns
    campaign_dirs = get_campaign_directories()
    
    if not campaign_dirs:
        print("No campaigns found. Please create a campaign first using 'angreal new campaign'.")
        return
    
    # If campaign not specified, prompt user to select
    if not campaign:
        print("Available campaigns:")
        for i, campaign_dir in enumerate(campaign_dirs, 1):
            print(f"{i}. {campaign_dir}")
        
        try:
            choice = int(input("Select a campaign (number): "))
            if 1 <= choice <= len(campaign_dirs):
                campaign = campaign_dirs[choice - 1]
            else:
                print("Invalid selection.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    elif campaign not in campaign_dirs:
        print(f"Campaign '{campaign}' not found.")
        return
    
    # Get next module number
    module_dirs = glob.glob(f"{campaign}/modules/[0-9][0-9]-*/")
    
    module_numbers = []
    for module_dir in module_dirs:
        match = re.search(r'/(\d+)-', module_dir)
        if match:
            module_numbers.append(int(match.group(1)))
    
    next_number = max(module_numbers) + 1 if module_numbers else 1
    
    # Convert module name to kebab-case
    module_slug = name.lower().replace(' ', '-')
    
    # Create module directory
    module_dir = f"{campaign}/modules/{next_number:02d}-{module_slug}"
    
    # Create subdirectories
    subdirs = [
        "maps",
        "handouts",
        "encounters"
    ]
    
    for subdir in subdirs:
        Path(f"{module_dir}/{subdir}").mkdir(parents=True, exist_ok=True)
    
    # Load module template from file
    module_template_path = os.path.join(angreal.get_root(), "templates", "module.md")
    with open(module_template_path, "r") as template_file:
        module_content = template_file.read().format(name=name)
    
    # Write module file
    os.makedirs(module_dir, exist_ok=True)
    module_file_path = f"{module_dir}/module.md"
    with open(module_file_path, "w") as f:
        f.write(module_content)
    
    # Load encounters template from file
    encounters_template_path = os.path.join(angreal.get_root(), "templates", "encounters.md")
    with open(encounters_template_path, "r") as template_file:
        encounter_template = template_file.read().format(name=name)
    
    with open(f"{module_dir}/encounters/encounters.md", "w") as f:
        f.write(encounter_template)
    
    print(f"Module '{name}' created successfully at {module_dir}/")
    print(f"Created main module file: {module_file_path}")
    print(f"Created subdirectories: {', '.join(subdirs)}")
    print("Next steps:")
    print("1. Fill out the module overview and adventure summary")
    print("2. Create maps and place them in the maps directory")
    print("3. Design encounters and add them to the encounters directory")