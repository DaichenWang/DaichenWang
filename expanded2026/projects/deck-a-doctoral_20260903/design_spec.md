<!-- ppt-master-schema: design-spec/v1 -->
# deck-a-doctoral - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | deck-a-doctoral |
| Canvas Format | PPT 16:9, 1280x720 |
| Page Count | 11 |
| Primary Language | en-AU |
| Target Audience | Expanded 2026 delegates at the Conference on Animation and Interactive Art, Linz — XR artists and researchers, digital-heritage and HCI academics, and doctoral peers and panel members in the consortium session; fluent in immersive practice, largely unfamiliar with Chinese diaspora studies and classical garden theory |
| Communication Intent | First make the doctoral inquiry's motivation and research gap legible to an XR audience with no background in diaspora studies; then account for the three-phase evidence base and its current status; then position three transferable contributions and invite methodological critique of the co-design model |
| Desired Audience Outcome | Delegates can restate root-seeking as the activation of sensory and embodied memory, name what each of the three phases produced, and identify which parts of the work travel beyond this garden and this diaspora |
| Core Message / Ask / Action | If root-seeking runs through sensory and embodied memory rather than physical location, the question is not where it can happen but how — and a co-designed XR garden is one testable answer |
| Delivery Context | Presenter-led ten-minute conference talk with live projection, Expanded 2026, Linz, 9–11 September 2026; secondary use as a doctoral-consortium discussion artifact |
| Artifact Afterlife | Hand-off to supervisors and the consortium panel; individual slides reused in candidature milestone documents |
| Reading Mode | presentation |
| Content Strategy | Stay close to the submitted paper's claims and figures; re-sequence them into a spoken ten-minute arc and lead with the personal motivation the paper opens on; no fact, figure or claim beyond the paper and the thesis |
| Design Style | Grid-locked academic white field with QUT blue as the only saturated colour and the garden renders as the sole full-colour events |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — explicit user instruction to write a script under every page |
| Custom Animations | disabled — workflow default |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-03 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 x 720 |
| viewBox | `0 0 1280 720` |
| Margins | 72px left and right, 56px top, 56px bottom |
| Content Area | x 72–1208, y 56–664 (1136 x 608) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative, pyramid
- **Mode Behavior**: Open on the lived moment that started the inquiry and hold that tension across the first two pages, then switch to conclusion-first exposition — gap, question, method, evidence, status — so every later page states its claim in the title and supports it beneath; close by resolving the opening tension into the three contributions and what generalises.
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, data-journalism
- **Visual Style Behavior**: A grid-locked white field with a short QUT-blue rule under each page title and a generous outer margin; content sits in two or three columns aligned to one shared grid; evidence pages carry compact labelled figures, inline source lines, and numerals set well above their captions; no cards, no rounded containers, no shadow and no gradient — separation comes from whitespace, hairline rules and a single pale surface panel used at most once per page.
- **Theme**: An academic white field in which the only saturated colour is QUT blue, and the garden renders are the sole full-colour events.
- **Tone**: Measured and plain, first-person only where the motivation demands it.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | Page field on every slide |
| Secondary background | #F2F5F8 | Pale surface panel lifting one evidence block per page |
| Primary | #003B71 | QUT blue — page titles, title rules, primary data marks, cover field |
| Accent | #0091DA | QUT support sky blue — the one highlighted data mark or emphasised term per page |
| Secondary accent | #8A8D8F | QUT silver — comparison and secondary data marks, de-emphasised series |
| Body text | #1A1A1A | Body copy and figure labels |
| Secondary text | #5A6570 | Captions, annotations, source lines, running foot |
| Divider | #D8DFE6 | Hairline rules and column separators |
| Grid | #E8EDF2 | Chart gridlines and axis ticks, lighter than dividers |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Serif / editorial-academic, sturdy at projection distance | Georgia | — | serif |
| Body | Humanist sans / neutral, quiet beside the serif | Calibri | — | sans-serif |
| Display | Serif / editorial-academic at architectural scale | Georgia | — | serif |

- **Title stack**: Georgia, serif
- **Body stack**: Calibri, sans-serif
- **Display stack**: Georgia, serif

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Display | 72 |
| Data | 56 |
| Title | 48 |
| Subtitle | 36 |
| Lead | 34 |
| Body | 28 |
| Annotation | 22 |
| Footnote | 16 |

- **Role rationale**: Display carries the cover title and the two oversized pull statements; Data carries hero numerals on the evidence and status pages; Display takes the Title serif so the cover and the pull statements keep the deck's editorial voice; Data stays on the body sans because Georgia sets non-lining figures, which read poorly at hero scale.

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: The page's claim reads first at top-left, evidence resolves left to right across the grid, and the source or qualifier line settles on the baseline.
- **Composition tendency**: One focal claim per page with its evidence set beside or beneath it; on evidence pages the figure takes the wider column and the interpretation the narrower one.
- **Cross-page continuity**: A short QUT-blue rule under every page title, a right-aligned slide number with a short running title at the foot, and at most one pale surface panel per page.
- **Spacing posture**: Open throughout, tightening only on the two evidence-dense pages.
- **Spacing anchors**: page margin 72px; block gap 32px; column gutter 32px; corner radius 0px; body leading 40px.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-filled/home.svg | Home, dwelling, the place of return |
| icons/tabler-filled/map-pin.svg | A located site, fieldwork location |
| icons/tabler-filled/user.svg | Participants, individual respondents |
| icons/tabler-filled/world.svg | The global diaspora, transnational reach |
| icons/tabler-filled/mountain.svg | Borrowed scenery, the Xishan prospect, landscape |
| icons/tabler-filled/headphones.svg | Spatial audio, listening conditions |
| icons/tabler-filled/microphone.svg | Interviews, focus-group discussion, dialect recordings |
| icons/tabler-filled/clock-hour-3.svg | Temporal change, day-night cycle, phase timing |
| icons/tabler-filled/message.svg | Conversation, the AI cultural guide, message boards |
| icons/tabler-filled/photo.svg | Captured imagery, visual documentation |
| icons/tabler-filled/database.svg | The scanned-artifact archive |
| icons/tabler-filled/archive.svg | Heritage record, durable collection |
| icons/tabler-filled/device-desktop.svg | Desktop fallback mode, platform delivery |
| icons/tabler-filled/plane.svg | Migration, distance, the flight back |
| icons/tabler-filled/bulb.svg | Contribution, insight, what the work adds |
| icons/tabler-filled/compass.svg | Orientation, research direction, next steps |
| icons/tabler-filled/chart-dots-2.svg | Survey evidence, quantitative pattern |
| icons/tabler-filled/sparkles.svg | Speculative or imagined space |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P07 | chart | horizontal_bar_chart | Rank the twelve on-site visitor items by mean agreement so the descent from cultural importance to personal significance is visible in one read |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vr_garden_hero.png | 1910x1069 | 1.79 | The reconstructed Jichang Garden in VR — the work's single most recognisable image | Placed | Wide band across the lower cover; on P08 a large left-column view paired with the Minecraft still | adaptive | user | Existing | Author's own Unity/VRChat capture of the Root-Seeking VR environment | no-text | P01 cover band; P08 VR platform evidence |
| minecraft_ai_guide.png | 703x337 | 2.09 | The Minecraft platform with the MinePal AI cultural guide answering in-world | Placed | Right-column companion to the VR view, kept small because the source is low resolution | no-crop | user | Existing | Author's own screen capture of the MinePal exchange about Li Bai and moonlight | preserve | P08 Minecraft platform evidence |
| p02_wuxi_station.png | reserved | reserved | The Wuxi Railway Station / Chunyun moment that opens the talk | Placeholder | Full-height right panel beside the opening statement | adaptive | placeholder | Placeholder | Author to supply their own photograph of the 9 February 2026 station scene | no-text | P02 motivation |
| p09_exhibition.png | reserved | reserved | The VR environment publicly exhibited, or a participant in the Quest 3 headset | Placeholder | Small evidence still beside the current-status list | adaptive | placeholder | Placeholder | Author to supply their own exhibition or headset-in-use photograph | no-text | P09 current status |

## IX. Content Outline

### Part 1: The question the work begins from

#### Slide 01 - Cover

- **Audience move**: Arriving with no context → holding the project's name, its site, and the claim the next ten minutes will test
- **Relationships**: none
- **Composition**: Title block on the upper white field, the VR garden as a wide band beneath it, authorship and conference line on the baseline
- **Cover impact**: The hook is the reconstructed garden itself set against the plain academic field — the audience sees the speculative space before hearing a word about it
- **Title**: Root-Seeking · Xun Gen
- **Core message**: A practice-based inquiry into XR environments for diasporic cultural reconnection
- **Content**: Full title / subtitle · Daichen Wang, School of Creative Arts, Queensland University of Technology · Expanded 2026, Linz, 9–11 September 2026
- **Images**: vr_garden_hero.png as the lower band

#### Slide 02 - Why this research exists

- **Audience move**: Treating this as another heritage-VR project → understanding it starts from a specific unreturned journey
- **Relationships**: contrast between those for whom return is routine and those for whom it has become a periodic exception; that contrast is the stated starting point of the inquiry
- **Composition**: One oversized statement on the left, reserved photograph panel on the right, date and place as a quiet annotation
- **Title**: 9 February 2026, Wuxi Railway Station
- **Core message**: The crowd was returning home; I was not — and that tension is the research's lived starting point
- **Content**: The Lunar New Year rush at its peak · a flight back to Brisbane in a few days · the gap between return as a way of life and return as a periodic exception · the Chinese diaspora numbers in the tens of millions, and the desire to reconnect with cultural origins stays powerful and persistent
- **Images**: p02_wuxi_station.png reserved on the right
- **Fact IDs**: paper section 1 Motivation

#### Slide 03 - From roots to routes

- **Audience move**: Assuming homesickness is nostalgia → holding a theoretical model in which belonging is built, not travelled to
- **Relationships**: order — Fei's soil-bound Xiangtu society and its Chaxu Geju reach an explanatory limit for permanent migrants, which Clifford's routes and Brah's homing desire then answer, and which Connerton grounds in the body
- **Composition**: Three sequential positions across the grid, the middle one marking where the older frame stops
- **Title**: From the roots of soil to the routes of mobility
- **Core message**: Homing desire is a longing for belonging that transcends geography, not a desire to return to a place
- **Content**: Fei Xiaotong — identity, kinship and moral obligation inseparable from the land of birth; Chunyun as its most visible modern expression · the limit — for permanent transnational migrants the geographical centre has irreversibly shifted · Brah — home as "a mythic place of desire in the diasporic imagination", a feeling actively constructed rather than a location reached · Connerton — cultural memory inscribed in the body through habitual practice, so familiar spaces, sounds and spatial logics are how identity is recalled
- **Fact IDs**: paper refs 6, 4, 3, 5

### Part 2: What the study asks and how it answers

#### Slide 04 - The gap

- **Audience move**: Assuming XR heritage already covers this → seeing precisely what has not been built or evaluated
- **Relationships**: contrast — existing digital strategies sustain relationships but not embodied spatial familiarity; existing VR-for-diaspora work either lacked cultural specificity or narrowed to students
- **Composition**: A single negative claim held above two short evidence columns
- **Title**: What has not been built
- **Core message**: No peer-reviewed, empirically validated social VR environment has been designed for the cultural and spatial needs of the Chinese diaspora
- **Content**: WeChat, video conferencing and social media sustain relationships across distance — but cannot replicate the embodied spatial familiarity Fei identified as the bedrock of Xiangtu society · preliminary VR-for-diaspora studies either lacked cultural specificity or focused narrowly on student populations · no study centres the classical Chinese garden as a carrier for root-seeking and belonging
- **Fact IDs**: paper section 2, ref 8

#### Slide 05 - The questions

- **Audience move**: Following the argument → able to repeat the overarching question and the three that operationalise it
- **Relationships**: parent — one overarching question is operationalised through one designed case, under which three subsidiary questions sit
- **Composition**: The overarching question at display scale, the three subsidiary questions as a numbered set beneath it
- **Title**: The questions
- **Core message**: When permanent physical return is no longer viable, how can the sensory, spatial and social conditions of cultural belonging be reconstituted elsewhere?
- **Content**: Overarching question, set at display scale · operationalised through one designed case — how a virtual Chinese garden co-designed with the diaspora can support root-seeking · Q1 which cultural, spatial and sensory elements are essential · Q2 how participatory co-design engages diaspora communities in shaping culturally authentic XR · Q3 how participants experience the environment in terms of cultural belonging and emotional reconnection · the garden is an instrumental case, not the object of the thesis
- **Fact IDs**: paper section 2

#### Slide 06 - Three phases

- **Audience move**: Wondering whether this is practice or research → seeing a specific, ethics-approved evidence base with counted participants
- **Relationships**: order — Phase One establishes requirements and builds, Phase Two takes the prototype to the community, Phase Three evaluates inside the same sessions
- **Composition**: Three phase columns of equal width, each with its participant counts as a hero numeral above its description
- **Title**: A three-phase participatory design study
- **Core message**: Every design decision carried into the next build is documented against the participant input that motivated it
- **Content**: Phase One — global online survey, 206 questionnaires returned across two rounds and 172 retained; on-site fieldwork with 50 visitors and staff at Jichang Garden, 27 written questionnaires (15 visitors, 12 administrators); prototype demonstrations extended to 40 participants; expert interview on cultural authenticity · Phase Two — Brisbane, 20 June 2026, two prototype reflection and validation focus groups, N=12 in two groups of six, recruited through Chinese-language social media, the CSSA and a local table tennis club chosen deliberately to reach beyond student networks · Phase Three — pre- and post-experience state questionnaires plus a 26-item experience measure, integrated into the same sessions and read descriptively against the discussions · all data collection approved under QUT Human Research Ethics LR 2025-8766
- **Fact IDs**: paper section 3

#### Slide 07 - What the evidence asked for

- **Audience move**: Expecting designer intuition → seeing the design requirements arrive from the data, including a clear negative result
- **Relationships**: contrast — cultural importance rates highest while personal significance and emotional attachment fall away in the same respondents; the online survey then fixes what the design must and must not do
- **Composition**: The ranked visitor chart takes the wide left column, the online-survey requirements sit as a short annotated list on the right
- **Title**: The design requirements came from the data
- **Core message**: These findings challenged gamification-led approaches and pushed the prototype toward ritual-based, affective engagement
- **Content**: On-site visitors, N=15 — gardens are important in Chinese culture 4.47 with 93.3% agreement, the highest of twelve items · willing to visit a garden abroad 4.33 · visiting relieves pressure 4.33 with 86.7% agreement · but gardens hold special significance for me 3.53 and I feel emotionally attached 3.80, both under half agreeing · online survey, N=172 — seasonal change and the passage of time rated highest of the five cultural-authenticity items at 4.32, SD 0.68 · centrality of cultural symbols 4.25, SD 0.75 · 130 of 172 named overly complex operation as the interaction style they would most prefer to avoid
- **Visualization**: visitor-item-ranking — horizontal bars of the twelve on-site visitor means, ordered descending, with the two low-attachment items marked in the accent colour and the 4.47 item labelled; Native-ready: visitor-item-ranking=yes
- **Fact IDs**: paper section 3, Figure 2

#### Slide 08 - Two platforms, one environment

- **Audience move**: Picturing a single VR demo → understanding a deliberate pairing in which the second platform is a research instrument
- **Relationships**: contrast — the high-fidelity environment is built for presence, the block environment for authorship; membership — both are the same designed case
- **Composition**: Two unequal columns, the VR view dominant on the left and the Minecraft still smaller on the right, each with a short specification line
- **Title**: Two platforms, one environment
- **Core message**: The Minecraft platform is the methodological engine of Phase Two, not a secondary demonstration
- **Content**: High-fidelity VR — Unity 2022.3, deployed through VRChat for Meta Quest 3, 90fps within a 3m x 3m tracking volume, non-VR desktop fallback · Minecraft Java Edition with an AI cultural guide through MinePal, configured rather than engineered through a written character brief covering classical poetry, Daoist naturalism and classical garden design · coarse building blocks keep construction visible and reversible for participants without 3D modelling skills · message boards and personal courtyard spaces support asynchronous, participant-owned contributions
- **Images**: vr_garden_hero.png in the left column, minecraft_ai_guide.png at reduced scale on the right; the two are read as one paired specimen rather than a before-and-after
- **Fact IDs**: paper sections 3 and 4

### Part 3: Where it stands and what it contributes

#### Slide 09 - Where the work stands

- **Audience move**: Unsure how far along this is → holding a concrete completion state and one open analysis
- **Relationships**: membership — four completed components of one project, with the thematic analysis the single item still in progress
- **Composition**: A short status list with the four hero numerals aligned, the in-progress item marked distinctly
- **Title**: Current status
- **Core message**: Data collection is complete; the thematic analysis now drives every remaining iteration
- **Content**: Data collection complete across all three phases; thematic analysis of the June 2026 focus-group data underway · VR environment fully operational, 90fps on Meta Quest 3, publicly exhibited · Minecraft platform with the MinePal guide complete, over 90% conversational accuracy across approximately 20 test rounds · digital archive of 102 scanned artifacts from Jichang Garden — handheld iPhone LiDAR, Gaussian Splatting and aerial photogrammetry — publicly accessible on Sketchfab · a third platform iteration in Unreal Engine in development · longitudinal co-creation phase running through the second half of 2026
- **Images**: p09_exhibition.png reserved beside the list
- **Fact IDs**: paper section 4

#### Slide 10 - Three contributions

- **Audience move**: Seeing an interesting artwork → able to name which field each contribution is addressed to and what generalises
- **Relationships**: parent — three contributions, each addressed to a distinct field; contrast — the empirical finding stays situated while the theory and the method are designed to travel
- **Composition**: Three equal columns, each headed by its field and carrying one claim, with the generalisation line running beneath all three
- **Title**: Three contributions, three fields
- **Core message**: The empirical findings are situated in this case; the theoretical model and the methodology are designed to travel
- **Content**: To diaspora and memory studies — a theoretical model of diasporic root-seeking as sensory and embodied memory activation, bringing Fei's Xiangtu into dialogue with Brah's homing desire · to digital heritage and HCI — to our knowledge the first peer-reviewed, empirically evaluated social VR environment tailored to Chinese diaspora cultural needs · to community-centred design practice — a validated co-design model for culturally specific XR, replicable with other displaced communities
- **Fact IDs**: paper section 5

#### Slide 11 - Next steps

- **Audience move**: Holding the contributions → knowing what happens next and leaving with the governing claim
- **Relationships**: order — complete the analysis, iterate both platforms, compare across three, then extend into embodied performance
- **Composition**: A short forward sequence across the page with the closing claim set at display scale beneath it
- **Closing impact**: The binding takeaway is that root-seeking's question is how and under what conditions, not where — stated as the last line the audience reads
- **Title**: Next steps
- **Core message**: If root-seeking operates through sensory memory rather than physical location, the question is not where it can happen, but how
- **Content**: Complete the thematic analysis, which drives iterative updates to both XR platforms · triangulate questionnaire patterns with discussion themes to compare how embodied VR presence and socially oriented Minecraft interaction shape root-seeking differently · the Unreal Engine version for higher visual fidelity, then comparative analysis across all three platforms · a planned collaboration with the QUT XR Screen Futures Hub and a local Chinese classical dance crew, motion-captured at The Block on QUT's Kelvin Grove campus, bringing classical dance into both platforms as a periodic cultural event · acknowledgement of supervisors Dr Rewa Wright, Professor Damian Candusso and Professor Gavin Sade, and of the staff and visitors of Jichang Garden
- **Fact IDs**: paper section 5, Acknowledgments

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: A verbatim-speakable English script for each page, grounded only in the submitted paper and the thesis; every number spoken aloud matches the page and the source exactly; each note opens with the transition from the previous page and closes on the sentence that hands over to the next; the reserved-photograph slots are listed in the handover summary and labelled on the slides themselves, so the spoken script stays clean
- **Total duration**: 10 minutes across 11 slides — roughly 55 seconds per page, with the cover under 20 seconds and the two evidence pages allowed 70
- **Notes style**: Conversational academic — first person on the motivation and the contributions, plain declarative elsewhere; written to be read aloud, not summarised
- **Presentation purpose**: Make the inquiry's motivation and gap legible to an XR audience, account for the three-phase evidence base and its status, and position three transferable contributions for critique
