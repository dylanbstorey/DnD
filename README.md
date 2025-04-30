# D&D Campaign Repository Guide

This guide explains how to effectively use this repository for managing Dungeons & Dragons campaigns. It covers both the organization structure and common workflows for campaign development and gameplay.

## Repository Structure

```
DnD/
├── campaign-title/                    # the campaign campaign
│   ├── README.md                      # Campaign overview
│   ├── campaign/                      # Campaign-wide resources
│   │   ├── overview.md                # High-level campaign synopsis
│   │   ├── timeline.md                # Campaign timeline
│   │   ├── world/                     # World building elements
│   │   │   ├── locations.md
│   │   │   ├── factions.md
│   │   │   └── maps/
│   │   └── lore/                      # Campaign-specific lore
│   ├── characters/                    # Character information
│   │   ├── progression-tracker.md     # Track character advancement
│   │   ├── [character-name]/          # Individual PC folders
│   │   │   ├── level-01.md            # Character sheets by level
│   │   │   ├── level-03.md
│   │   │   └── character-art.jpg
│   │   └── npcs/                      # Non-player characters
│   │       ├── allies/
│   │       └── villains/
│   ├── modules/                       # Adventure modules
│   │   ├── 00-campaign-reference/     # Shared resources
│   │   │   ├── monsters/
│   │   │   ├── npcs/
│   │   │   └── mechanics/
│   │   ├── 01-module-name/            # Individual adventure modules
│   │   │   ├── module.md              # Main adventure text
│   │   │   ├── maps/
│   │   │   └── handouts/
│   │   └── 02-module-name/
│   └── sessions/                      # Actual gameplay records
│       ├── session-log.md             # Quick reference of all sessions
│       └── session-01/                # Individual session folders
│           └── session-01.md          # Combined prep/notes/recap
└── campaign-resources/                # Shared resources across campaigns
    ├── house-rules/                   # Custom rules
    ├── name-generators/               # Quick reference for naming
    ├── random-tables/                 # Generic encounter tables, etc.
    └── templates/                     # Reusable document templates
```

## Common Workflows

### Campaign Development

#### 1. Initial Campaign Setup

```bash
angreal new campaign
```

After running these scripts:
1. Edit the campaign `overview.md` to establish the campaign premise
2. Create a basic `timeline.md` with major historical events
3. Populate initial world building files with key locations and factions

#### 2. Creating a New Adventure Module

1. `angreal new module`
2. Fill in the module details, including:
   - Main adventure text
   - Maps and visual aids
   - Monster stat blocks (or reference existing ones)
   - NPC information
   - Puzzles and challenges

#### 3. Adding NPCs and Monsters

For reusable creatures:
1. Create stat blocks in `modules/00-campaign-reference/monsters/`
2. Use consistent formatting following D&D 5e stat block conventions

For campaign-specific NPCs:
1. Create character sheets in `characters/npcs/allies/` or `characters/npcs/villains/`
2. Include personality traits, motivations, and knowledge

### Session Management

#### 1. Before a Session

1. Create a new session via `angreal new session`
2. Fill out the preparation section:
   - Story progression expected
   - NPCs and locations to feature
   - Encounters and challenges
   - Rewards and loot
   - Contingency plans

#### 2. During a Session

1. Take notes in the session file's "Session Notes" section
2. Track:
   - Actual events (timeline)
   - Player decisions and consequences
   - Combat results
   - Improvised elements
   - Questions to research later

#### 3. After a Session

1. Complete the "Session Recap" section:
   - Write narrative summary
   - Update quest progress
   - Note character development
   - Document rewards earned
   - Plan for next session
2. Update the master `session-log.md` with a brief summary
3. Update character sheets if significant advancement occurred
4. Update campaign timeline if major events occurred

#### 4. Character Advancement

When characters level up:
1. Create new level-specific character sheets in each PC's folder
2. Update the progression-tracker.md with milestones reached
3. Note any significant character development in the session recap

