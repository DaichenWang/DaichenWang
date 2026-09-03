<!-- ppt-master-schema: design-spec/v1 -->
# deck-b-artwork - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | deck-b-artwork |
| Canvas Format | PPT 16:9, 1280x720 |
| Page Count | 11 |
| Primary Language | en-AU |
| Target Audience | Expanded 2026 delegates at the Conference on Animation and Interactive Art, Linz — XR artists, interactive-art practitioners, digital-heritage and critical-heritage researchers; interested in how the work is made and what it claims, comfortable with real-time engines and capture pipelines |
| Communication Intent | Present Root-Seeking · Xun Gen as a finished operational artwork rather than a research programme: show what it is and what it feels like, defend the position that separates speculative co-creation from appropriation, explain the dual-platform and capture decisions in enough technical detail to be reused, and state honestly what the findings do and do not yet establish |
| Desired Audience Outcome | Delegates can describe the dual-platform model and why the two environments are paired, explain the layered-provenance answer to the appropriation question, and repeat the recognition-versus-attachment finding as a caution about how virtual heritage is evaluated |
| Core Message / Ask / Action | A heritage site can be reimagined as a postgeographic sanctuary — a living counter-archive co-created with the community it serves — and the pairing of a high-fidelity contemplative world with a low-barrier co-creative one is the transferable part |
| Delivery Context | Presenter-led ten-minute conference talk with live projection, Expanded 2026, Linz, 9–11 September 2026; secondary use as a project showcase for collaborators and the XR Screen Futures Hub |
| Artifact Afterlife | Reuse as the project's standing introduction deck; individual technical slides reused in collaborator and funding conversations |
| Reading Mode | presentation |
| Content Strategy | Stay close to the submitted paper's claims, figures and technical values; re-sequence them so the work is seen before it is theorised, and keep the paper's own stated limitations rather than smoothing them; no fact, figure or claim beyond the paper and the thesis |
| Design Style | Image-led academic white field where the garden renders run to the page edge and QUT blue carries every structural mark |
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
- **Mode References**: showcase, instructional
- **Mode Behavior**: Lead with the work itself at full visual scale for two pages so the audience has something to hold, then alternate — each conceptual or technical page states one idea and decomposes it into its parts step by step, with an image page resetting the rhythm between the harder blocks; close by naming the three registers of contribution and the limit of what the findings support.
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, photo-editorial
- **Visual Style Behavior**: The same grid-locked white field and hairline discipline as its companion deck, but photography is allowed to lead — the garden renders run full-bleed or to a hard page edge on the image pages, with type set on a solid QUT-blue plate or clear white margin rather than over the picture; text pages stay austere, two- or three-column, with a short QUT-blue rule under the title; no cards, no rounded containers, no shadow and no gradient, and no image is ever tinted or overlaid with a scrim.
- **Theme**: An austere white publication in which the garden is permitted to take the whole page whenever it is the argument.
- **Tone**: Confident about the making, plainly honest about the limits.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | Page field on text pages |
| Secondary background | #F2F5F8 | Pale surface panel behind one technical block per page |
| Primary | #003B71 | QUT blue — page titles, title rules, type plates over imagery, primary data marks |
| Accent | #0091DA | QUT support sky blue — the highlighted data mark and the one emphasised term per page |
| Secondary accent | #8A8D8F | QUT silver — comparison data marks, secondary treemap cells, de-emphasised series |
| Body text | #1A1A1A | Body copy and figure labels |
| Secondary text | #5A6570 | Captions, annotations, source lines, running foot |
| Divider | #D8DFE6 | Hairline rules and column separators |
| Grid | #E8EDF2 | Chart gridlines, axis ticks and treemap cell separations |

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

- **Role rationale**: Display carries the cover title and the two full-bleed statements set on the blue plate; Data carries the hero numerals on the findings and digitisation pages; Display takes the Title serif so the cover and the pull statements keep the deck's editorial voice; Data stays on the body sans because Georgia sets non-lining figures, which read poorly at hero scale.

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: On text pages the claim reads first at top-left and decomposes downward; on image pages the picture reads first and the type block anchors one corner.
- **Composition tendency**: Alternate a wide-visual page against a two- or three-column explanation page, so no two consecutive pages carry the same weight.
- **Cross-page continuity**: A short QUT-blue rule under every text-page title, a right-aligned slide number with a short running title at the foot, and the same hard page-edge alignment for every image.
- **Spacing posture**: Variable by page rhythm — austere and open on text pages, edge-to-edge on image pages.
- **Spacing anchors**: page margin 72px; block gap 32px; column gutter 32px; corner radius 0px; body leading 40px.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-filled/home.svg | Home, dwelling, the place of return |
| icons/tabler-filled/map-pin.svg | The located site, Jichang Garden itself |
| icons/tabler-filled/user.svg | Individual visitors, respondents |
| icons/tabler-filled/world.svg | The global diaspora, multilingual reach |
| icons/tabler-filled/mountain.svg | Borrowed scenery, the Xishan prospect, aerial perspective |
| icons/tabler-filled/headphones.svg | Spatial audio, Pingtan, dialectal fragments |
| icons/tabler-filled/microphone.svg | Voice chat, recorded poetry, field recordings |
| icons/tabler-filled/clock-hour-3.svg | The day-night cycle, temporal variation |
| icons/tabler-filled/message.svg | The AI cultural guide, message boards, conversation |
| icons/tabler-filled/photo.svg | Capture, photogrammetry, visual documentation |
| icons/tabler-filled/database.svg | The open archive of scanned artifacts |
| icons/tabler-filled/archive.svg | Counter-archive, durable heritage record |
| icons/tabler-filled/device-desktop.svg | Desktop fallback mode, platform delivery |
| icons/tabler-filled/plane.svg | Distance, the diaspora that cannot attend in person |
| icons/tabler-filled/bulb.svg | Contribution, what the project adds |
| icons/tabler-filled/compass.svg | Orientation, spatial logic, wayfinding |
| icons/tabler-filled/chart-dots-2.svg | Survey evidence, quantitative pattern |
| icons/tabler-filled/sparkles.svg | The speculative layer, imagined ritual |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P05 | chart | dumbbell_chart | Join each pair of values so the distance between recognition and attachment is the mark the audience reads |
| P09 | chart | treemap_chart | Encode the 102 digitised artifacts as six category areas so the dominance of architectural components is immediate |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vr_garden_hero.png | 1910x1069 | 1.79 | The reconstructed Jichang Garden in VR — the bridge, pavilion and borrowed prospect in one frame | Placed | Full-bleed cover field with the title on a solid blue plate; on P06 a large left view; on P08 a wide band supporting the aerial-perspective argument | adaptive | user | Existing | Author's own Unity/VRChat capture of the Root-Seeking VR environment | no-text | P01 cover; P06 presence column; P08 aerial perspective |
| vr_detail_blossom_path.png | 1911x1071 | 1.78 | The blossom path and red pavilion — the environment's atmosphere and depth at eye level | Placed | Wide edge-anchored view carrying the page, with the type block in one clear corner | adaptive | user | Existing | Author's own Unity/VRChat detail capture of the VR environment | no-text | P02 the work; P07 inside the environment |
| minecraft_ai_guide.png | 703x337 | 2.09 | The MinePal AI cultural guide answering in-world about Li Bai, moonlight and homesickness | Placed | Kept small and never enlarged past its native pixels; sits as the right-hand companion on P06 and as the evidence still on P10 | no-crop | user | Existing | Author's own screen capture of the MinePal exchange | preserve | P06 authorship column; P10 the Minecraft laboratory |
| p04_scanned_artifact.png | reserved | reserved | One scanned artifact, or the Sketchfab archive page, standing for the factual layer | Placeholder | Right-hand panel beside the two-layer provenance model | adaptive | placeholder | Placeholder | Author to supply their own Sketchfab capture or artifact render | no-text | P04 layered provenance |
| p09_capture_pipeline.png | reserved | reserved | Capture in the field — handheld LiDAR scanning, or the aerial capture over the garden | Placeholder | Small evidence still beside the three capture methods | adaptive | placeholder | Placeholder | Author to supply their own fieldwork photograph from the Jichang Garden digitisation | no-text | P09 digitisation pipeline |

## IX. Content Outline

### Part 1: The work

#### Slide 01 - Cover

- **Audience move**: Arriving with no context → standing inside the reconstructed garden before a single claim is made
- **Relationships**: none
- **Composition**: The garden render running to all four page edges, the title and authorship on a solid QUT-blue plate anchored to one side
- **Cover impact**: The hook is the garden at full page scale — this deck shows the work before it explains it
- **Title**: Root-Seeking · Xun Gen
- **Core message**: Reimagining a historic Chinese garden in XR
- **Content**: Full title / subtitle · Daichen Wang, Rewa Wright, Damian Candusso, Gavin Sade — School of Creative Arts, Queensland University of Technology · Expanded 2026, Linz, 9–11 September 2026
- **Images**: vr_garden_hero.png full-bleed

#### Slide 02 - What it is

- **Audience move**: Seeing a pretty garden → knowing exactly what platform, what device and what kind of experience this is
- **Relationships**: membership — one experiential environment whose named components are gesture, sound and poetic narrative
- **Composition**: The detail view carrying the page from one edge, a compact specification block in the clear corner
- **Title**: An experiential, multisensory environment
- **Core message**: Root-Seeking · Xun Gen takes its name from xun gen — the quest for cultural, historical and spiritual origins that runs through Chinese diaspora communities
- **Content**: Developed in Unity 2022.3, deployed on Meta Quest 3 · engages users through gesture, sound and poetic narrative interaction · draws on the aesthetics and spatial logics of Jichang Garden, one of the most celebrated classical literati gardens in China · the garden is both symbolic and technical scaffold for a virtual site of belonging · a parallel Minecraft platform extends the participatory scope
- **Images**: vr_detail_blossom_path.png anchored to the page edge
- **Fact IDs**: paper Abstract, section 1

#### Slide 03 - Not preservation — a spatial language spoken again

- **Audience move**: Filing this under virtual tourism or reconstruction → seeing a deliberate critical-heritage position with a stated limit
- **Relationships**: contrast — XR heritage research is oriented toward accurate reconstruction, education and virtual tourism, while this work addresses a displaced community and treats the garden as a language; link — that position obliges the stated limitation
- **Composition**: The position on the left at lead scale, the limitation held in a pale panel on the right so it reads as owned rather than buried
- **Title**: Addressed to a displaced community, not to tourists
- **Core message**: Heritage is a cultural process negotiated in the present, so interpretive authority shifts toward the diaspora itself
- **Content**: The field is oriented toward accurate reconstruction, education and virtual tourism, with a growing strand attending to emotional design · this project differs in audience and aim — the garden is not an object to be documented but a spatial language to be spoken again · Smith's critique of the authorised heritage discourse asks whose voices are centred; for diasporic communities, accounts anchored in national territory render their relationship to heritage secondary · community members are authors of the rituals, narratives and social practices that animate it, not recipients of a reconstructed garden · the limitation, stated: participation does not dissolve power relations — decisions about what was scanned, whose dialects are heard and which garden stands in for home were made by the research team, and a Jiangnan literati garden cannot represent the regional diversity of Chinese heritage
- **Fact IDs**: paper section 1, refs 4, 7, 1

#### Slide 04 - Layered provenance

- **Audience move**: Suspecting that speculation compromises the record → holding a concrete two-layer answer they could apply themselves
- **Relationships**: parent — a factual layer anchors the environment and a speculative layer is built on it; contrast — one remains record, the other remains legible as interpretation
- **Composition**: Two stacked layers reading bottom-up, the factual base wider than the speculative layer above it, with the reserved artifact image alongside
- **Title**: What separates speculative co-creation from distortion
- **Core message**: Participants are given licence to imagine precisely because imagining does not overwrite the historical record
- **Content**: Factual layer — an open archive of 102 systematically scanned artifacts, anchoring the environment in the physical garden and remaining publicly inspectable · speculative layer — community-authored ritual, narrative and atmosphere built on that foundation and remaining legible as interpretation rather than record · keeping the two distinct lets the work operate simultaneously as archive and as artwork
- **Images**: p04_scanned_artifact.png reserved on the right
- **Fact IDs**: paper section 1, ref 8

### Part 2: What the audience asked for, and what was built

#### Slide 05 - Recognition is not attachment

- **Audience move**: Assuming cultural importance implies personal connection → holding the study's most consequential and least comfortable result
- **Relationships**: contrast — the same respondents at the same sitting rate cultural importance high and personal significance low; contrast — sustained professional involvement shifts attachment sharply
- **Composition**: The paired-value chart across the wide left column, the design consequences as a short list on the right
- **Title**: Recognition runs ahead of attachment
- **Core message**: A virtual heritage environment can secure recognition without securing attachment — and that matters for how this work is evaluated
- **Content**: Visitors, N=15 — cultural importance 4.47 with 93.3% agreement, but gardens hold special significance for me 3.53 and emotional attachment 3.80, each with fewer than half agreeing · administrators, N=12, whose involvement is sustained and professional — emotional attachment 4.50 with unanimous agreement · attachment varies among people who share a nationality, a language and a location · both groups rated sensory experience as the most important quality of a virtual garden, 4.20 and 4.25, while reporting almost no prior VR use, naming insect sound, birdsong and the scent of flowering shrubs · the online survey, N=172 — seasonal change and the passage of time highest at 4.32, SD 0.68; cultural symbols 4.25, SD 0.75; strict adherence to traditional design principles lowest and widest at 3.70, SD 1.10 · the clearest result was negative — 130 of 172 named overly complex operation as the interaction style to avoid, ahead of excessive gamification at 86 and excessive modernity at 56, in a sample where 40.1% had never used a VR device
- **Visualization**: recognition-attachment-gap — paired value marks joined by a rule, one pair for visitors' cultural importance against personal significance and one for emotional attachment across visitors and administrators, with the joining distance carrying the meaning; Native-ready: recognition-attachment-gap=no — the closed native chart payload has no paired-value connector type, so forcing it into a bar or scatter would drop the joining mark that carries the finding
- **Fact IDs**: paper section 1, Table 1

#### Slide 06 - Presence and authorship

- **Audience move**: Reading two platforms as redundancy → understanding a designed opposition of affordances
- **Relationships**: contrast — the high-fidelity environment affords presence and signals a finished world, the block environment affords authorship and signals an unfinished one
- **Composition**: Two columns of unequal weight, each headed by the affordance it carries, with the pull statement running beneath both
- **Title**: Realism is received; blocks are remade
- **Core message**: Realism communicates that heritage is to be received; blocks communicate that heritage may be remade
- **Content**: The VRChat environment is the primary aesthetic interface for individual contemplation — continuous space, naturalistic scale and vegetation, spatialised sound position the user as an embodied visitor, and its visual completeness signals a finished world that invites contemplation rather than alteration · the Minecraft environment is a low-barrier social laboratory — its coarse block grammar makes construction legible and reversible, lowers the skill threshold for building, supports persistent shared worlds, and signals that the world is open to change · the pairing rests on this affordance analysis and on the survey requirement for a low operational threshold, not on measured preference · whether the two serve different audience segments is what the 2026 co-creation workshops are designed to examine
- **Images**: vr_garden_hero.png in the presence column, minecraft_ai_guide.png at native scale in the authorship column
- **Fact IDs**: paper section 2

#### Slide 07 - Inside the environment

- **Audience move**: Knowing the concept → able to picture the actual minute-to-minute experience and its deliberate refusals
- **Relationships**: membership — the interactive elements, the audio layer and the temporal cycle are components of one contemplative design; contrast — what the environment deliberately omits
- **Composition**: The detail view carrying the page from the edge, the specification and the three refusals set in the clear margin
- **Title**: No score, no timer, no failure state
- **Core message**: Contemplative engagement was prioritised over task-oriented interaction, against the clearest result in the survey
- **Content**: Open-world environment on Meta Quest 3, up to three concurrent users, free exploration within a 3m x 3m tracking volume, 90fps with assets optimised for mobile GPU constraints, non-VR desktop fallback · approaching specific heritage artifacts triggers readings of Classical Chinese poetry in Mandarin and local dialects · spatial audio including Suzhou Pingtan music and dialectal voice fragments distributed contextually across the environment · a dynamic day-night cycle shifts lighting and ambient sound, embodying the passage of time central to root-seeking · multi-user capability enables spontaneous social encounters and voice chat · there is no score, no timer and no failure state
- **Images**: vr_detail_blossom_path.png anchored to the page edge
- **Fact IDs**: paper section 2

#### Slide 08 - Aerial perspective is a cultural decision

- **Audience move**: Reading fog as a rendering trick → seeing one technical fix that is simultaneously an argument about ways of seeing
- **Relationships**: link — a flattening effect prompted a lighting change, which turns out to restore a culturally specific way of rendering depth
- **Composition**: The garden band running wide across the page with the argument set beneath it in two short movements, optical then cultural
- **Title**: Depth through mist, not perspective
- **Core message**: Restoring aerial perspective both improves depth perception and recovers a culturally specific way of seeing
- **Content**: A flattening effect was observed under uniform illumination, where equal lighting across the depth scale reduced the legibility of distance · distance-based volumetric fog and height fog now attenuate contrast and saturation toward the horizon, so dark, saturated foreground elements recede into progressively hazier distant scenery · this adjustment is cultural as much as optical — classical shanshui landscape painting renders depth through mist and tonal recession rather than linear perspective · Jichang Garden itself borrows the distant Xishan hills through atmospheric haze
- **Images**: vr_garden_hero.png as a wide band
- **Fact IDs**: paper section 3

### Part 3: The archive, the laboratory, and what it contributes

#### Slide 09 - 102 artifacts

- **Audience move**: Hearing "we scanned the garden" → holding the actual composition, the three capture methods and their honest constraints
- **Relationships**: membership — 102 objects across six functional categories; order — three capture methods matched to scale and complexity; contrast — what the pipeline could not capture at all
- **Composition**: The category areas across the wide left column, the capture methods and constraints as a short sequence on the right
- **Title**: Digitising the garden
- **Core message**: To our knowledge the most comprehensive volumetric archive of Jichang Garden in existence — and the distribution reflects the conditions of capture as much as the site
- **Content**: 102 heritage objects across six categories assigned by function — architectural components 47, garden furniture and functional objects 16, sculpture and decorative elements 11, inscriptions plaques and calligraphy 11, plants and natural landscape 9, architecture and spatial structures 8 · handheld iPhone LiDAR for standard objects at ground level such as stone guardian lions and bridge structures · Gaussian Splatting processed in Scaniverse for intricate surface detail and challenging light · aerial video reconstructed as photogrammetric geometry for spatial relationships and the borrowed prospect toward the Xishan hills · high-resolution models averaging 50,000 polygons decimated to 5,000–8,000 by quadric edge collapse, UV mapping preserved for 4K texture atlases · vegetation resists photogrammetry entirely, so every tree in the built environments is a procedural model · the point-based volumetric nature of Gaussian Splatting mirrors the fragmented, fluid nature of diasporic memory — heritage as a reconstructing field of light and data rather than a solid, immutable object
- **Visualization**: artifact-category-composition — six nested area cells sized by object count, the 47-object category dominant and labelled, the rest ordered clockwise by count; Native-ready: artifact-category-composition=no — the native treemap payload rejects per-cell data labels, and the six counts are the point of the figure
- **Images**: p09_capture_pipeline.png reserved beside the capture methods
- **Fact IDs**: paper sections 4 and 5

#### Slide 10 - The Minecraft laboratory

- **Audience move**: Treating the AI guide as a gimmick → seeing a configured, briefed cultural agent inside a participatory workshop instrument
- **Relationships**: membership — server, agent, message boards, voice and personal courtyards are components of one co-creation environment; link — the character brief is what makes the agent culturally accountable
- **Composition**: The in-world capture at native scale on one side, the configuration and the workshop plan as a short list on the other
- **Title**: Configured, not engineered
- **Core message**: The project supplies a written character brief; the service holds it as the agent's standing instruction
- **Content**: Minecraft Java Edition with custom server deployment, integrating an AI cultural guide through the MinePal service as an in-world NPC capable of natural language conversation about garden aesthetics, classical poetry and Chinese philosophical traditions · multilingual interaction with language switching on request · the brief covers classical poetry, Daoist naturalism and classical garden design principles, written against curated cultural references with attention to data governance and the cultural representativeness of generated content · message boards for asynchronous community dialogue, real-time voice communication, and personal courtyard spaces for participant customisation · workshops scheduled for the second half of 2026 will engage participants in collaboratively designing ritualised activities, social mechanics and narrative elements
- **Images**: minecraft_ai_guide.png at native scale
- **Fact IDs**: paper section 2

#### Slide 11 - Postgeographic sanctuaries

- **Audience move**: Holding the parts → able to name three registers of contribution and the exact boundary of what has been shown
- **Relationships**: parent — three registers of contribution; contrast — what the findings establish against what still awaits the post-workshop evaluation
- **Composition**: Three short columns for the registers with the boundary statement beneath them and the closing claim at display scale
- **Closing impact**: The binding takeaway is heritage sites reimagined as postgeographic sanctuaries — living counter-archives co-created with the communities they serve
- **Title**: What this contributes, and what it does not yet show
- **Core message**: Heritage sites can be reimagined as postgeographic sanctuaries: living counter-archives co-created with the communities they serve
- **Content**: Empirically — what this audience wants from virtual heritage: contemplative rather than gamified interaction, temporal rhythm, cultural symbolism, sensory content beyond the visual, and a low operational threshold · as design research — a transferable dual-platform strategy pairing a high-fidelity contemplative environment with a low-barrier co-creative one, connected by a participatory pipeline in which community-authored content migrates into the crafted world · as arts practice — a model of cultural XR privileging affect, ritual and multisensory engagement over photorealism, shifting the discourse from heritage documentation to heritage invention · the boundary, stated: these findings establish need, design preferences and initial reception, not long-term effect — claims about identity formation and durable reconnection await the post-workshop evaluation · the open archive of 102 artifacts extends the impact beyond the VR experience itself · grounded in a single garden and a single diaspora, the model of participatory grounding, layered provenance and paired platforms is designed to travel
- **Fact IDs**: paper section 5

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: A verbatim-speakable English script for each page, grounded only in the submitted paper and the thesis; every number spoken aloud matches the page and the source exactly; the limitation and boundary statements are spoken as written rather than softened; each note opens with the transition from the previous page and closes on the sentence that hands over to the next; the reserved-photograph slots are listed in the handover summary and labelled on the slides themselves, so the spoken script stays clean
- **Total duration**: 10 minutes across 11 slides — roughly 55 seconds per page, with the cover under 20 seconds and the findings and digitisation pages allowed 70
- **Notes style**: Conversational academic in the first person plural, since the paper is co-authored; confident on the making, plain and unhedged on the limits
- **Presentation purpose**: Show the work before theorising it, defend the layered-provenance position, explain the dual-platform and capture decisions well enough to be reused, and state honestly what the findings do and do not establish
