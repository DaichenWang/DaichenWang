# 01_cover

This is Root-Seeking, Xun Gen. Xun gen means root-seeking — the search for where you come from. What you're looking at is not a photograph. It's our reconstruction of Jichang Garden in Wuxi, captured inside VRChat, and you can walk into it wearing a headset. I'm Daichen Wang, with Rewa Wright, Damian Candusso and Gavin Sade at QUT.

---

# 02_the_work

Let me tell you what it is before I tell you what it argues. It is built in Unity 2022.3 and it runs on Meta Quest 3. You move through it with your hands, you hear it, and poetry comes up as you go. It takes its look and its sense of space from Jichang Garden, and I want to be clear about that relationship. We did not photograph the garden as a subject. The garden is both a symbol and a structure — it gives the virtual place its grammar: framed views, borrowed scenery, and a view held back and then given to you.

---

# 03_not_preservation

Now the position, because it is not the usual one. Most XR heritage work aims at accurate rebuilding, teaching and virtual tourism. We differ in who it is for and what it is for: made for a community living far from home rather than for tourists, and treating the garden not as an object to record but as a language of space to speak again. That comes out of critical heritage studies: heritage is something people work out in the present, and Smith asks whose voices sit at the centre of it. So we move that authority towards the community. And on the right is the part we are not going to smooth over. Taking part does not remove power, and we do not claim it does. What got scanned, whose dialects you hear, which garden stands in for home — our team decided all of that. One garden from one region cannot stand in for all of Chinese heritage.

---

# 04_layered_provenance

Which raises the question you should be asking. If we invite people to imagine things about a real heritage site, what stops that from becoming distortion? Our answer is to keep two layers apart. Underneath is the factual layer: a hundred and two objects, all scanned the same way and published openly. That is the archive on the right — every object with its own page, its own view count, its own comments. Anyone can check what we say. On top of it is the imagined layer: ritual, story and atmosphere written by the community, and clearly marked as interpretation, not as record. That separation is what lets this be an archive and an artwork at once. People are free to imagine because imagining does not paint over the record underneath.

---

# 05_recognition_attachment

This is the finding that shaped the project most, and it is the least comfortable one. On the left, two pairs of numbers. The top pair is visitors at the garden. They rate how important the Chinese garden is to the culture at four point four seven, with ninety-three per cent agreeing — the highest of twelve items. But how much it means to them personally sits at three point five three. That gap is inside the same people, at the same sitting. The lower pair is the one question both surveys share: emotional attachment. Visitors give three point eight. Staff give four point five, and every one of them agreed. Working with a place for years moves attachment. Sharing a country, a language and a postcode does not. So knowing something matters runs ahead of feeling close to it, and that changes how work like ours should be judged: a virtual heritage space can win recognition without winning attachment. On the right, what follows. Both groups said the senses matter most — insect sound, birdsong, the smell of flowers — though almost none of them had used VR before. And the clearest answer in the survey was negative: a hundred and thirty out of a hundred and seventy-two said avoid making it too complicated.

---

# 06_presence_authorship

So we built two worlds, and the pair is an argument, not a hedge. The VRChat world is about being there: unbroken space, natural scale, real planting, sound that comes from where the thing is. It puts you in the place as a visitor, and because it looks finished, it tells you to look, not to touch. The Minecraft world is about making: rough blocks make building easy to read and easy to undo, they lower the skill you need, and they say the world is unfinished and open. To be honest, our demonstrations tested the work as one thing, so this pairing rests on what each medium invites, plus that survey result about keeping it simple — not on measured preference. The line at the bottom is the short version. Realism says heritage is something you receive. Blocks say heritage is something you can remake.

---

# 07_inside_environment

Here is what a session is actually like. Up to three people at once on Quest 3, exploring freely in a three by three metre space, at ninety frames a second, with a desktop mode so you do not need a headset to get in. Walk up to an object and it reads you classical Chinese poetry, in Mandarin and in local dialects. Suzhou Pingtan singing and pieces of dialect sit in particular spots, so the sound comes from places rather than from everywhere at once. And the light you are looking at is the day and night cycle. It changes the lighting and the sound, which is how time gets into a place that would otherwise be frozen. Then the three things we left out, in the title. No score, no timer, no way to fail. That came straight out of the clearest result in our survey.

---

# 08_aerial_perspective

One technical decision that turned out to be more than technical. With even lighting everywhere, the place went flat. The same light at every distance, and you stopped being able to read depth. The fix was fog — fog that builds with distance, and fog that sits low — pulling contrast and colour out of things as they go towards the horizon. But look at what that brings back. Classical Chinese landscape painting, shanshui, shows depth through mist and fading tone rather than through lines running to a vanishing point. And Jichang Garden itself borrows the Xishan hills in the distance through haze — that is the view on screen, and the whole garden is composed around it. So the fix improves depth and recovers a way of seeing at the same time.

---

# 09_digitising

The factual layer, in detail. A hundred and two heritage objects, digitised into six groups, sorted by what each object does in the garden. The biggest block is building parts, forty-seven — and that split says as much about how we captured things as about the site: those parts are many, separate and easy to reach, while the two smallest groups are the hardest to record. Three methods. A handheld iPhone LiDAR scanner for things at ground level, the stone lions and the bridges. Gaussian Splatting, processed in Scaniverse, for fine surfaces and awkward light. And drone video turned into models for the borrowed view. Plants defeat photo-based scanning completely, so every tree here is generated. And Gaussian Splatting gives us more than accuracy. It is made of points and light rather than solid surfaces, a lot like memory when you live far from home: broken up, and moving.

---

# 10_minecraft_lab

The Minecraft side runs on Java Edition with our own server, and it carries an AI cultural guide through a service called MinePal — a character in the world who will talk with you about garden design, classical poetry and Chinese philosophy, and switch language if you ask. The word I want to insist on is configured, not built. We give it a written character brief — classical poetry, Daoist ideas about nature, garden design principles — and the service holds that brief as the character's standing instruction. We wrote it against a chosen set of cultural sources, with attention to how the data is handled and to how well what it says represents the culture. Around that character sit message boards, live voice, and private courtyards people decorate themselves. That is what makes this a workshop tool, not a feature.

---

# 11_contribution

Three things, and then a limit. As evidence, we show what this audience wants from virtual heritage: something calm rather than a game, a sense of time passing, cultural symbols, sound and other senses beyond sight, and a low bar to get in. As design research, the two-platform model is the part you could take away — a high-detail, quiet world paired with an easy, build-it-together one, joined by a pipeline that carries what the community makes into the crafted world. As arts practice, an XR work that puts feeling and ritual ahead of photorealism. Now the limit, and I would rather say it than have you find it. These findings show need, design preferences and first reactions. They do not show long-term effect. Anything about identity or lasting reconnection waits on the evaluation after the workshops. What we are proposing is that heritage places can be rebuilt as sanctuaries that do not depend on geography: living counter-archives, made with the communities they are for. Thank you.
