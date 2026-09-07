# 01_cover

This is Root-Seeking, Xun Gen. Xun gen means root-seeking — the search for where you come from. What you're looking at is not a photograph. It's our reconstruction of Jichang Garden in Wuxi, captured inside VRChat, and you can walk into it wearing a headset. I'm Daichen Wang, with Rewa Wright, Damian Candusso and Gavin Sade at QUT.

---

# 02_the_work

Let me tell you what it actually is before I tell you what it argues. It is built in Unity 2022.3 and deployed on Meta Quest 3. It is experiential and multisensory: you move through it with gesture, you hear it, and poetry surfaces as you go. It draws on the aesthetics and the spatial logics of Jichang Garden, and I want to be precise about the relationship there. The garden is not a subject we photographed. It is both a symbolic and a technical scaffold — the thing that gives the virtual site its grammar of framed views, borrowed scenery, and revelation withheld and then granted.

---

# 03_not_preservation

Now the position, because it is not the usual one. XR heritage research points mostly at accurate reconstruction, education and virtual tourism. We differ in audience and in aim: addressed to a displaced community rather than tourists, treating the garden not as an object to document but as a spatial language to be spoken again. That follows critical heritage studies — heritage is a process through which belonging gets negotiated now, and Smith's critique of authorised heritage discourse asks whose voices are centred. So interpretive authority shifts toward the diaspora. And on the right is the part we are not going to smooth over. Participation does not dissolve power relations and we do not claim it does. What got scanned, whose dialects you hear, which garden stands in for home — the research team decided all of that. One Jiangnan literati garden cannot represent the regional diversity of Chinese heritage.

---

# 04_layered_provenance

Which raises the question you should be asking. If we are inviting people to speculate on a real heritage site, what separates that from distortion? Our answer is a layered model of provenance. Underneath, the factual layer: a hundred and two systematically scanned artifacts, published openly. That is the repository on the right — every object with its own page, its own view count, its own comment thread. Anyone can check what we claim. On top of it, the speculative layer: ritual, narrative and atmosphere authored by the community, and deliberately legible as interpretation rather than as record. Keeping those two apart is what lets the work be an archive and an artwork at the same time. Participants are given licence to imagine precisely because imagining does not overwrite the record underneath.

---

# 05_recognition_attachment

This is the result that has shaped the project most, and it is the least comfortable one. On the left, two pairs of values. The top pair is visitors on site: they rate the cultural importance of the Chinese garden at four point four seven, ninety-three per cent agreement, the highest of twelve items — but personal significance for them, individually, sits at three point five three. That gap is in the same people at the same sitting. The lower pair is the one item both questionnaires share, emotional attachment: visitors at three point eight, administrators at four point five with unanimous agreement. Sustained, professional involvement moves attachment; sharing a nationality, a language and a location does not. So recognition runs ahead of attachment, and that matters for how work like ours gets evaluated: a virtual heritage environment can secure recognition without securing attachment. On the right, what follows. Both groups rated sensory experience the most important quality of a virtual garden while reporting almost no prior VR use — insect sound, birdsong, the scent of flowering shrubs. And the clearest result in the online survey was negative: a hundred and thirty of a hundred and seventy-two named overly complex operation as the thing to avoid.

---

# 06_presence_authorship

So we built two environments, and the pairing is an argument about affordances rather than a hedge. The VRChat world affords presence: continuous space, naturalistic scale and vegetation, spatialised sound. It positions you as an embodied visitor, and its visual completeness signals a finished world — something to be contemplated, not altered. The Minecraft world affords authorship: coarse blocks make construction legible and reversible, they lower the skill threshold for building, and they signal that the world is unfinished and open. To be honest: our demonstrations evaluated the virtual version as one object, so this pairing rests on affordance analysis and the survey's low-threshold requirement, not on measured preference. The line at the bottom is the compressed version. Realism communicates that heritage is to be received. Blocks communicate that heritage may be remade.

---

# 07_inside_environment

Here is what a session is actually like. Up to three concurrent users on Quest 3, free exploration inside a three by three metre volume at ninety frames per second, with a non-VR desktop mode so the work is not gated on owning a headset. Approach a heritage artifact and it triggers a reading of classical Chinese poetry, in Mandarin and in local dialects. Suzhou Pingtan and fragments of dialectal voice are distributed across the space, so the soundtrack is positional rather than ambient wallpaper. And the light you are looking at is the day-night cycle — it shifts the lighting and the ambient sound, which is how the passage of time gets into a space that would otherwise be frozen. And then the three refusals in the title. There is no score, no timer, and no failure state. That was a decision taken directly against the clearest result in our survey data.

---

# 08_aerial_perspective

One technical decision that turned out to be more than technical. Under uniform illumination the environment flattened — equal lighting across the whole depth scale, and distance stopped being legible. The fix was distance-based volumetric fog and height fog, attenuating contrast and saturation toward the horizon, so dark saturated foreground elements recede into progressively hazier distance. But look at what that actually restores. Classical shanshui landscape painting renders depth through mist and tonal recession rather than through linear perspective. And Jichang Garden itself borrows the distant Xishan hills through atmospheric haze — that is the view on screen, and that borrowed prospect is what the whole composition is built around. So restoring aerial perspective improves depth perception and recovers a culturally specific way of seeing at the same time.

---

# 09_digitising

The factual layer, in detail. A hundred and two heritage objects, digitised across six categories assigned by the function each object performs in the garden. The dominant block is architectural components, forty-seven — and that distribution reflects the conditions of capture as much as the site: those are numerous, discrete and reachable, while the two smallest categories are the two hardest to record. Three capture methods. Handheld iPhone LiDAR for objects at ground level, stone guardian lions and bridges. Gaussian Splatting, processed in Scaniverse, for intricate surfaces and difficult light. Aerial video reconstructed as photogrammetry for the borrowed prospect. Vegetation resists photogrammetry entirely, so every tree here is procedural. And there is something beyond fidelity in the Gaussian Splatting: its point-based volumetric nature mirrors the fragmented, fluid quality of diasporic memory. Heritage as a reconstructing field of light and data, not a solid immutable object.

---

# 10_minecraft_lab

The Minecraft side runs on Java Edition with a custom server, and it carries an AI cultural guide through the MinePal service — an in-world character who will hold a conversation about garden aesthetics, classical poetry and Chinese philosophical traditions, and switch language on request. The phrase I want to insist on is configured, not engineered. We supply a written character brief covering classical poetry, Daoist naturalism and classical garden design principles, and the service holds that brief as the agent's standing instruction. It was written against curated cultural references, with attention to data governance and to how representative the generated content actually is. Around the agent sit message boards for asynchronous dialogue, real-time voice, and personal courtyard spaces participants customise themselves — which is what makes this a workshop instrument rather than a feature.

---

# 11_contribution

Three registers, and then a boundary. Empirically, we document what this audience wants from virtual heritage: contemplative rather than gamified interaction, temporal rhythm, cultural symbolism, sensory content beyond the visual, and a low operational threshold. As design research, the dual-platform model is the transferable part — a high-fidelity contemplative environment paired with a low-barrier co-creative one, joined by a pipeline that moves community-authored content into the crafted world. As arts practice, a cultural XR that privileges affect and ritual over photorealism, shifting from heritage documentation toward heritage invention. Now the boundary, and I would rather state it than have you find it. These findings establish need, design preferences and initial reception. They do not establish long-term effect. Claims about identity formation and durable cultural reconnection wait on the post-workshop evaluation. What we are proposing, in the end, is that heritage sites can be reimagined as postgeographic sanctuaries: living counter-archives, co-created with the communities they serve. Thank you.
