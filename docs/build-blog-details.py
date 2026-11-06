import os
import pathlib

ROOT = pathlib.Path(r"c:\Users\HP\Downloads\millstone-atta-template\millstone-atta-template")

POSTS = [
    {
        "id": 1,
        "file": "blog-details.html",
        "title_head": "Dressing Millstones by Hand — Millstone & Co.",
        "desc_head": "Why Meera re-cuts the furrows in our granite stones by hand and how that slow craft keeps your stone-ground flour cool, fragrant and soft.",
        "heading": "Why we still dress our millstones by hand",
        "category": "Milling",
        "date": "12 Oct 2026",
        "read_time": "6 min read",
        "author": "Meera Kapoor",
        "role": "Head Miller",
        "initials": "MK",
        "color1": "#c9a24b",
        "color2": "#7a5a1e",
        "image": "assets/images/photo-010.jpg",
        "image_alt": "Traditional stone mill used for grinding grains.",
        "caption": "Hand-dressing re-cuts the master furrows so wheat berries shear gently without friction heat.",
        "author_bio": "Meera is Millstone's Head Miller. She joined the mill in 2009, launched our whole-millet range and still inspects the first handful of flour from every morning batch by hand.",
        "prev_file": "blog-details-9.html",
        "prev_title": "Meet the team behind Granary Lane",
        "next_file": "blog-details-2.html",
        "next_title": "Bran, germ and endosperm: in your atta",
        "intro": "Every three to four weeks, our two pairs of 750-kilogram granite stones go quiet. We hoist the runner stone using heavy block-and-tackle, wipe away the fine flour film, and set out a set of hardened steel mill picks. What follows is two full days of deliberate, rhythmic tapping: hand-dressing the stones.",
        "body_html": """
            <h2>The anatomy of a living stone</h2>
            <p>A chakki stone is not flat. It is carved with a radial pattern of lands and furrows. The deep valleys (furrows) scoop fresh grain from the eye, funnel cooling air between the stones, and distribute the cracked berries outward. The raised flat plateaus (lands) perform the actual shearing action that rubs the bran and endosperm into microscopic flakes.</p>
            <p>Over hundreds of hours of grinding hard whole wheat, the sharp cutting edges of these furrows gradually glaze over and turn slick. When a millstone glazes, it stops cutting cleanly and begins to crush by brute compression. That compression generates destructive heat.</p>

            <blockquote>A dull stone cooks flour inside the mill; a sharp, dressed stone glides through grain like scissors through silk.</blockquote>

            <h2>Why modern machinery cannot replace the mill pick</h2>
            <p>Visitors frequently ask why we don't dress our stones with electric diamond angle-grinders or computerized laser cutters. The answer comes down to micro-texture:</p>
            <ol>
              <li><strong>Micro-grooves over glass glaze:</strong> Hand picks create microscopic pitting that grabs the wheat kernel instead of letting it slip and burn.</li>
              <li><strong>Graduated furrow depth:</strong> Near the eye, furrows must be 12 mm deep to accept whole grain; at the skirt, they taper to less than 1.5 mm to polish the flour. No machine matches a miller's touch for that graduation.</li>
              <li><strong>Zero heat stress on the granite:</strong> High-speed power tools heat the natural stone locally, which can cause micro-fractures in the crystalline quartz structure.</li>
              <li><strong>True balance:</strong> Hand-dressing preserves the dynamic balance of the turning stone, preventing harmonic vibration that causes uneven flour fineness.</li>
            </ol>

            <figure class="my-4">
              <div class="ph ph-flour ph-wide" role="img" aria-label="Freshly dressed millstone face showing precise furrow patterns."><img class="ph-photo" src="assets/images/photo-051.jpg" alt="Freshly dressed millstone face showing precise furrow patterns." loading="lazy" decoding="async"></div>
              <figcaption class="meta mt-2 text-center text-muted">The lands and furrows carved into natural Indian granite stones at Granary Lane.</figcaption>
            </figure>

            <h2>The thermometer test</h2>
            <p>The proof of sharp stones is in the palm of your hand. When our stones are freshly dressed, flour leaves the spout at between 34 °C and 38 °C — barely warmer than body temperature. The natural oils inside the germ remain cool and stable, retaining their sweet, grassy perfume and vitamin E content.</p>
            <p>When you open your monthly sack of Millstone atta, that buttery aroma is directly attributable to the two days Meera spent with her steel hammers.</p>

            <h2>How stone-dressing affects your dough</h2>
            <p>Because hand-dressed stones produce clean, flaked bran rather than pulverized powder, the bran particles have softer edges. They don't sever the gluten strands as you knead your dough, allowing rotis to trap steam and balloon into pillowy, paper-thin phulkas with ease.</p>
        """
    },
    {
        "id": 2,
        "file": "blog-details-2.html",
        "title_head": "Bran, Germ & Endosperm Guide — Millstone & Co.",
        "desc_head": "A plain-language look at the three anatomy parts of a whole wheat berry and what each layer brings to your rotis, digestion and nutrition.",
        "heading": "Bran, germ and endosperm: what is actually in your atta",
        "category": "Nutrition",
        "date": "5 Oct 2026",
        "read_time": "7 min read",
        "author": "Noa Levi",
        "role": "Grain Sourcing & Nutrition Lead",
        "initials": "NL",
        "color1": "#5b7c4b",
        "color2": "#2f4e22",
        "image": "assets/images/photo-017.jpg",
        "image_alt": "Top view of various seeds and grains displayed in ceramic bowls on a white background.",
        "caption": "The complete wheat berry broken down into its three nutritional components: outer bran, vitamin-packed germ, and starchy endosperm.",
        "author_bio": "Noa holds a master's degree in food agronomy and heads grain sourcing at Millstone. She tests every incoming farm harvest for moisture, protein and mineral density.",
        "prev_file": "blog-details.html",
        "prev_title": "Why we still dress our millstones by hand",
        "next_file": "blog-details-3.html",
        "next_title": "Soft phulka rotis: the 70% hydration method",
        "intro": "When you buy supermarket flour, the ingredient list usually says 'whole wheat flour'. But under modern commercial milling standards, that term legally allows manufacturers to separate all three anatomical parts of the grain, strip out the delicate germ to prolong shelf life, and recombine only whatever proportions they choose. Here is what is truly inside a whole grain.",
        "body_html": """
            <h2>The three distinct layers of a wheat berry</h2>
            <p>Every single kernel of Sharbati wheat is a self-contained biological seed, engineered by nature to protect, nourish, and sprout a new plant. It consists of three distinct parts:</p>

            <div class="row g-4 my-3">
              <div class="col-md-4">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <h3 class="h6 fw-bold text-primary mb-2">1. The Bran (14%)</h3>
                  <p class="small text-muted mb-0">The hard outer jacket. Loaded with dietary prebiotic fibre, B-complex vitamins, trace minerals (iron, zinc, magnesium), and phytochemical antioxidants.</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <h3 class="h6 fw-bold text-primary mb-2">2. The Germ (3%)</h3>
                  <p class="small text-muted mb-0">The tiny embryonic sprout. Contains concentrated vitamin E, essential omega fatty acids, natural folate, and rich nutty oils that define real flour flavour.</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <h3 class="h6 fw-bold text-primary mb-2">3. The Endosperm (83%)</h3>
                  <p class="small text-muted mb-0">The energy reserve. Composed of complex starch granules surrounded by gluten-forming proteins (gliadin and glutenin) that provide dough elasticity.</p>
                </div>
              </div>
            </div>

            <blockquote>When you remove the germ to make flour last six months in a warehouse, you throw out 80% of the flavour and the heart of the nutrition.</blockquote>

            <h2>Why commercial roller mills extract the germ</h2>
            <p>Wheat germ oil is rich in polyunsaturated fats. The moment the germ is crushed, enzymes called lipases begin breaking down these fats, creating natural oxidation. In fresh stone-ground flour, this provides a delightful sweet hazelnut aroma for the first 3 to 4 weeks.</p>
            <p>However, industrial supply chains demand a 12-month shelf life. In roller mills, high-velocity fluted steel cylinders shatter the kernel, air sifters extract the oily germ, and white starch is separated. Even when packaged as 'whole wheat', the germ oil is usually either missing or heat-stabilized, losing its live enzyme activity.</p>

            <h2>Nutritional comparison per 100g</h2>
            <div class="table-responsive my-4">
              <table class="table compare-table">
                <thead><tr><th scope="col">Nutrient</th><th scope="col">Millstone 100% Chakki Atta</th><th scope="col">Commercial Whole Wheat</th><th scope="col">Refined White Flour (Maida)</th></tr></thead>
                <tbody>
                  <tr><th scope="row">Dietary Fibre</th><td>12.8 g</td><td>8.5 g</td><td>2.7 g</td></tr>
                  <tr><th scope="row">Vitamin E (tocopherols)</th><td>1.4 mg</td><td>0.3 mg</td><td>Traces</td></tr>
                  <tr><th scope="row">Magnesium</th><td>138 mg</td><td>72 mg</td><td>22 mg</td></tr>
                  <tr><th scope="row">Natural Germ Oil</th><td>Fully retained (raw)</td><td>De-germed / toasted</td><td>Zero</td></tr>
                </tbody>
              </table>
            </div>

            <h2>How whole germ changes your cooking</h2>
            <p>Because our stone mills rub the germ evenly across every starch particle, the dough absorbs water more gradually and forms an exceptionally pliable network. The rotis you roll will not turn leathery as they cool in your tiffin box.</p>
        """
    },
    {
        "id": 3,
        "file": "blog-details-3.html",
        "title_head": "Soft Phulka Rotis: 70% Hydration — Millstone & Co.",
        "desc_head": "Our foolproof step-by-step method for rotis that puff on the open flame and stay soft in the lunch dabba until evening.",
        "heading": "Soft phulka rotis: the 70% hydration method",
        "category": "Recipes",
        "date": "28 Sep 2026",
        "read_time": "5 min read",
        "author": "Layla Haddad",
        "role": "Recipe Developer & Baker",
        "initials": "LH",
        "color1": "#d2691e",
        "color2": "#8b3a0e",
        "image": "assets/images/photo-067.jpg",
        "image_alt": "A cook lifts a chapati from a hot pan.",
        "caption": "A light touch, balanced water ratio, and a gentle turn on direct flame make the perfect puffed roti.",
        "author_bio": "Layla develops all bakery recipes and kitchen ratios for Millstone. Her background combines traditional Middle Eastern flatbreads with classical Indian chakki flours.",
        "prev_file": "blog-details-2.html",
        "prev_title": "Bran, germ and endosperm: in your atta",
        "next_file": "blog-details-4.html",
        "next_title": "Visiting farms behind our Sharbati wheat",
        "intro": "The biggest misconception about making soft rotis is that you need oil, ghee, or milk in the dough. You do not. All you need is fresh stone-ground flour, the correct water-to-flour ratio by weight, and a patient rest period for gluten hydration.",
        "body_html": """
            <h2>The golden formula: 70% hydration</h2>
            <p>Hydration simply means the weight of water relative to the weight of flour. Stone-ground whole wheat atta contains the intact outer bran and germ, both of which are thirstier than commercial bleached flour. If you only use 55% water, the bran steals moisture from the starch, leaving the cooked roti dry and brittle.</p>
            <p>For every <strong>100 grams of Millstone Sharbati Atta</strong>, use exactly <strong>70 grams (or ml) of warm water</strong>. For an average family batch of 8 rotis (250 g flour), use 175 ml of warm water.</p>

            <h2>The 4 essential steps</h2>
            <ol>
              <li><strong>The Initial Mix (2 minutes):</strong> Add 80% of the water to the flour in a wide parat. Mix with your fingers until a rough, shaggy mass forms. Sprinkle the remaining 20% over dry pockets. Do not knead aggressively yet!</li>
              <li><strong>The 15-Minute Autolyse:</strong> Cover the rough dough with a damp muslin cloth and walk away for 15 minutes. During this rest, the bran softens and gluten bonds form naturally without mechanical sweat.</li>
              <li><strong>The Quick Knead (3 minutes):</strong> Return to the bowl. Punch down with your knuckles for just 2 to 3 minutes. You will feel the dough transform into a silky, supple dough that springs back when pressed.</li>
              <li><strong>Rolling without excess dry flour:</strong> Roll lightly with wrist pressure from center outward. Dust only once with dry flour; excessive dry flour scorches on the tawa and creates bitter spots.</li>
            </ol>

            <blockquote>Steam is the only leavening agent in a phulka. If your tawa is hot enough, trapped steam inflates the two layers into a sphere within three seconds.</blockquote>

            <h2>Tawa timing and flame transition</h2>
            <p>Preheat a heavy cast iron tawa until a drop of water sizzles and dances. Place your rolled roti gently:</p>
            <ul>
              <li><strong>Side 1 (15-20 seconds):</strong> Wait until tiny pale blisters appear on the surface. Flip immediately.</li>
              <li><strong>Side 2 (30-40 seconds):</strong> Cook until golden-brown freckles develop underneath. Press the edges gently with a clean cloth.</li>
              <li><strong>The Flame (3-5 seconds):</strong> Transfer directly onto a medium open burner flame with tongs. Watch it balloon completely, then transfer to an insulated roti dabba lined with a cotton towel.</li>
            </ul>

            <figure class="my-4">
              <div class="ph ph-roti ph-wide" role="img" aria-label="Cooked hot rotis with melted homemade ghee."><img class="ph-photo" src="assets/images/photo-022.jpg" alt="Cooked hot rotis with melted homemade ghee." loading="lazy" decoding="async"></div>
              <figcaption class="meta mt-2 text-center text-muted">A light brush of cultured A2 ghee seals in moisture while preserving the crisp outer skin.</figcaption>
            </figure>

            <h2>Why they stay soft until lunchtime</h2>
            <p>Because the 70% hydration gelled the starch completely during cooking, moisture is locked inside the molecular matrix. Even four hours later in an office tiffin, your phulkas will tear like silk.</p>
        """
    },
    {
        "id": 4,
        "file": "blog-details-4.html",
        "title_head": "Farms Behind Our Sharbati Wheat — Millstone & Co.",
        "desc_head": "Noa spent harvest week with our partner farmers in Sehore, Madhya Pradesh. Here is what we learned from soil tests and this year's harvest.",
        "heading": "Visiting farms behind our Sharbati wheat",
        "category": "Sourcing",
        "date": "19 Sep 2026",
        "read_time": "8 min read",
        "author": "Noa Levi",
        "role": "Grain Sourcing & Nutrition Lead",
        "initials": "NL",
        "color1": "#5b7c4b",
        "color2": "#2f4e22",
        "image": "assets/images/photo-019.jpg",
        "image_alt": "A wide rural landscape of wheat fields beneath a blue sky.",
        "caption": "The deep black cotton soil of the Malwa plateau, where rain-fed Sharbati wheat develops its distinctive golden lustre.",
        "author_bio": "Noa oversees our direct-farm procurement contracts, soil microbiome partnerships, and regenerative grain quality audits across Central India.",
        "prev_file": "blog-details-3.html",
        "prev_title": "Soft phulka rotis: the 70% hydration method",
        "next_file": "blog-details-5.html",
        "next_title": "Saturday evening windows are now open",
        "intro": "Every March and April, the black soil of the Sehore plateau in Madhya Pradesh turns into an endless sea of amber. This is the home of Sharbati wheat — often called the 'golden grain of India'. Last month, I spent seven days with the three farming families who supply over 60% of Millstone's wheat.",
        "body_html": """
            <h2>The soil that makes wheat naturally sweet</h2>
            <p>Why does Sharbati wheat taste distinctly sweeter and yield softer dough than grain grown in canal-irrigated plains? The secret is in the geology of the Malwa plateau. The soil here is heavy black basaltic clay (vertisol), formed from ancient volcanic lava flows.</p>
            <p>This soil has extraordinary moisture-holding capacity. Our partner farmers do not flood their fields with chemical tube-well water; instead, the wheat roots drink deeply from the moisture trapped deep in the black earth during the monsoon. The slow, water-stressed ripening period forces the plant to concentrate natural sucrose and complex oligosaccharides in the berry.</p>

            <h2>Meeting farmer Rameshwar and his third-generation fields</h2>
            <p>On our second morning in Ashta, Rameshwar Patel walked us through his 24-acre heirloom parcel. Rameshwar's grandfather began farming with native indigenous seeds in 1964. Today, Rameshwar uses zero synthetic chemical insecticides, relying instead on neem-cake manure, cow dung bio-slurry, and companion pulses that fix atmospheric nitrogen naturally.</p>

            <blockquote>When you touch the soil and it smells like sweet rain rather than synthetic ammonia, you know the flour will nourish the child who eats it.</blockquote>

            <h2>What we test in every harvest lot</h2>
            <p>Before any grain truck departs the village for Granary Lane, we run a rigorous 5-point quality audit right in the farmyard:</p>
            <ol>
              <li><strong>Moisture Content:</strong> Must test between 10.5% and 11.8%. Higher moisture causes mold; lower makes grain shatter during milling.</li>
              <li><strong>Hectolitre Weight:</strong> We test test-weight per bushel. Sharbati must achieve > 81 kg/hL, indicating plump, nutrient-dense berries.</li>
              <li><strong>Protein Percentage:</strong> Target range is 12.2% to 13.5% gluten-forming protein with high extensibility.</li>
              <li><strong>Foreign Matter:</strong> Zero tolerance for stones, weed seeds, or broken chaff.</li>
              <li><strong>Organoleptic Chew Test:</strong> Rameshwar crushes raw kernels between his teeth; if it snaps crisp and turns sweet on the tongue, it passes.</li>
            </ol>

            <figure class="my-4">
              <div class="ph ph-field ph-wide" role="img" aria-label="Golden raw Sharbati wheat grains held in cupped hands."><img class="ph-photo" src="assets/images/photo-023.jpg" alt="Golden raw Sharbati wheat grains held in cupped hands." loading="lazy" decoding="async"></div>
              <figcaption class="meta mt-2 text-center text-muted">Cleaned, sun-dried Sharbati grains ready for transport in breathable jute sacks.</figcaption>
            </figure>

            <h2>Direct trade: fair pricing for regenerative care</h2>
            <p>By buying directly from twelve family farms without middlemen or mandi commissions, Millstone pays 25% above the government minimum support price. In return, our farmers commit to regenerative cover cropping, preserving the heritage soil for the generations to come.</p>
        """
    },
    {
        "id": 5,
        "file": "blog-details-5.html",
        "title_head": "Saturday Delivery Windows Open — Millstone & Co.",
        "desc_head": "From 7 November you can receive freshly stone-ground flour deliveries in a new Saturday evening 5-8 pm window across all delivery zones.",
        "heading": "Saturday evening windows are now open",
        "category": "Company news",
        "date": "10 Sep 2026",
        "read_time": "3 min read",
        "author": "Daniel Okafor",
        "role": "Logistics & Customer Operations",
        "initials": "DO",
        "color1": "#3b6e8c",
        "color2": "#1d4257",
        "image": "assets/images/photo-020.jpg",
        "image_alt": "A white delivery van parked under a tree on a sunny day in an urban area.",
        "caption": "Our temperature-controlled electric delivery vans now cover weekend evening routes throughout the metro area.",
        "author_bio": "Daniel manages delivery fleets, route dispatch, and subscriber scheduling at Millstone. He ensures every bag is delivered within 24 hours of milling.",
        "prev_file": "blog-details-4.html",
        "prev_title": "Visiting farms behind our Sharbati wheat",
        "next_file": "blog-details-6.html",
        "next_title": "How we keep flour below 40 degrees C",
        "intro": "Over the past six months, the most common feedback from our working subscribers has been clear: weekday morning deliveries can be tough to coordinate when leaving for the office. We listened. Starting Saturday, 7 November 2026, we are officially opening our new Saturday Evening (5:00 pm – 8:00 pm) delivery slot.",
        "body_html": """
            <h2>Why evening delivery was tricky to engineer</h2>
            <p>Because Millstone is committed to delivering within 24 hours of grinding, we don't hold standing inventory in a distribution depot. Grains ground at 6:00 am on Saturday morning must be rested, packed into our breathable unbleached paper bags, and loaded onto refrigerated vans by 3:30 pm.</p>
            <p>To enable the Saturday evening window, we have adjusted our weekend milling shift. Head Miller Meera and her team now run an early-morning Saturday milling batch dedicated entirely to evening subscriptions.</p>

            <h2>Available delivery slots overview</h2>
            <div class="table-responsive my-4">
              <table class="table compare-table">
                <thead><tr><th scope="col">Delivery Day</th><th scope="col">Morning Slot</th><th scope="col">Evening Slot</th><th scope="col">Milled On</th></tr></thead>
                <tbody>
                  <tr><th scope="row">Tuesday</th><td>7:00 am – 11:00 am</td><td>5:00 pm – 8:00 pm</td><td>Same day 5:00 am</td></tr>
                  <tr><th scope="row">Thursday</th><td>7:00 am – 11:00 am</td><td>5:00 pm – 8:00 pm</td><td>Same day 5:00 am</td></tr>
                  <tr><th scope="row">Saturday</th><td>7:00 am – 11:00 am</td><td><strong>5:00 pm – 8:00 pm (NEW!)</strong></td><td>Same day 6:00 am</td></tr>
                </tbody>
              </table>
            </div>

            <blockquote>When fresh warm flour arrives on Saturday evening, Sunday morning parathas and puris become a family ritual.</blockquote>

            <h2>How to switch your recurring delivery slot</h2>
            <p>If you already have an active bi-weekly or monthly delivery plan, switching to the new Saturday evening window takes ten seconds:</p>
            <ol>
              <li>Log in to your account via the <a href="login.html">Login Portal</a>.</li>
              <li>Go to your <a href="dashboard-schedule.html">Delivery Schedule</a> tab in the dashboard.</li>
              <li>Click <strong>Edit Delivery Slot</strong> and select 'Saturday 5:00 pm – 8:00 pm'.</li>
              <li>Confirm changes. Your next delivery on or after 7 November will automatically follow the new time.</li>
            </ol>

            <h2>Eco-friendly delivery vans</h2>
            <p>All Saturday evening deliveries will be serviced by our new fleet of 100% electric delivery vans. The cargo areas are kept insulated under 20 °C, ensuring that even during summer heatwaves, your flour arrives cool, fragrant, and ready for your dinner preparations.</p>
        """
    },
    {
        "id": 6,
        "file": "blog-details-6.html",
        "title_head": "Keeping Flour Below 40°C — Millstone & Co.",
        "desc_head": "Heat destroys wheat germ aromatics and vitamins. Here is how slow stone RPM, grain feed calibration and cooling bins protect every batch.",
        "heading": "How we keep flour below 40 degrees C",
        "category": "Milling",
        "date": "2 Sep 2026",
        "read_time": "6 min read",
        "author": "Meera Kapoor",
        "role": "Head Miller",
        "initials": "MK",
        "color1": "#c9a24b",
        "color2": "#7a5a1e",
        "image": "assets/images/photo-051.jpg",
        "image_alt": "Fresh wheat flour in a paper-lined container with a scoop.",
        "caption": "Calibrated stone speed and gentle air cooling maintain low temperature from grain hopper to packaging pouch.",
        "author_bio": "Meera is Millstone's Head Miller. She oversees temperature telemetry, grain tempering moisture, and stone maintenance across all three active chakki units.",
        "prev_file": "blog-details-5.html",
        "prev_title": "Saturday evening windows are now open",
        "next_file": "blog-details-7.html",
        "next_title": "Crisp ragi dosa with a fermented batter",
        "intro": "In commercial grain milling, speed is money. High-speed industrial roller mills and high-RPM electric chakkis spin at 800 to 1,400 revolutions per minute, ejecting flour at temperatures between 60 °C and 75 °C. At that heat, the delicate live oils in the wheat germ are practically cooked before they ever touch your kitchen pan.",
        "body_html": """
            <h2>The chemistry of milling heat</h2>
            <p>Wheat germ is packed with natural tocopherols (Vitamin E), polyunsaturated fatty acids, and active enzymes. When flour temperatures exceed 42 °C, three things begin to happen:</p>
            <ul>
              <li><strong>Thermal oxidation of germ oils:</strong> The rich, sweet hazelnut fragrance degrades into a flat, chalky aroma.</li>
              <li><strong>Premature starch gelatinization:</strong> Damaged starch loses its capacity to absorb water steadily during kneading.</li>
              <li><strong>Enzyme denaturation:</strong> Amylase enzymes that naturally break down starch into sweet malt sugars during dough resting are destroyed.</li>
            </ul>

            <blockquote>If flour feels uncomfortably hot to your bare palm as it leaves the chute, the mill has already killed its soul.</blockquote>

            <h2>Our three cold-milling safeguards</h2>
            <p>At Millstone & Co., we maintain a strict ceiling: <strong>flour never leaves the stone spout above 38.5 °C</strong>. To guarantee this across both summer and winter, we rely on three engineering practices:</p>

            <div class="row g-3 my-3">
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-light-subtle border">
                  <h3 class="h6 fw-bold text-primary">1. Ultra-Low RPM</h3>
                  <p class="small text-muted mb-0">Our 750 kg granite stones turn at an unhurried 280 RPM. Lower velocity reduces friction heat by over 65% compared to commercial chakkis.</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-light-subtle border">
                  <h3 class="h6 fw-bold text-primary">2. Measured Feed Rate</h3>
                  <p class="small text-muted mb-0">Vibratory hoppers feed whole grains at a steady 45 kg per hour, preventing grain bunching and friction bottlenecks between stones.</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-light-subtle border">
                  <h3 class="h6 fw-bold text-primary">3. Passive Aeration Trays</h3>
                  <p class="small text-muted mb-0">Flour flows over food-grade stainless cooling flumes where ambient filtered air brings temperature down to 24 °C before bagging.</p>
                </div>
              </div>
            </div>

            <h2>Live digital monitoring on every run</h2>
            <p>Every mill unit at Granary Lane is fitted with twin infrared thermal sensors positioned at the stone throat and the discharge chute. If flour temperature approaches 40 °C, the feed controller automatically throttles the grain flow and increases airflow.</p>

            <figure class="my-4">
              <div class="ph ph-flour ph-wide" role="img" aria-label="Miller inspecting fresh cool flour by hand."><img class="ph-photo" src="assets/images/photo-010.jpg" alt="Miller inspecting fresh cool flour by hand." loading="lazy" decoding="async"></div>
              <figcaption class="meta mt-2 text-center text-muted">A tactile check ensures silkiness without clumping or thermal starch damage.</figcaption>
            </figure>

            <h2>Taste the cold-milled difference</h2>
            <p>When you take your first bite of a roti made from cold-milled Sharbati atta, the difference is immediate: clean wheat sweetness, zero bitterness, and a supple chew that keeps fresh all day.</p>
        """
    },
    {
        "id": 7,
        "file": "blog-details-7.html",
        "title_head": "Crisp Ragi Dosa Recipe — Millstone & Co.",
        "desc_head": "How to make crisp, golden finger-millet dosas with a naturally fermented batter using fresh stone-ground ragi flour from Granary Lane.",
        "heading": "Crisp ragi dosa with a fermented batter",
        "category": "Recipes",
        "date": "24 Aug 2026",
        "read_time": "4 min read",
        "author": "Layla Haddad",
        "role": "Recipe Developer & Baker",
        "initials": "LH",
        "color1": "#d2691e",
        "color2": "#8b3a0e",
        "image": "assets/images/photo-022.jpg",
        "image_alt": "Top view of a traditional South Indian dosa meal with chutneys and sambar.",
        "caption": "Crispy paper-thin ragi dosa served with fresh coconut chutney, tomato onion relish, and piping hot lentil sambar.",
        "author_bio": "Layla develops wholesome grain recipes for Millstone's recipe library, pairing ancestral grains with simple modern cooking techniques.",
        "prev_file": "blog-details-6.html",
        "prev_title": "How we keep flour below 40 degrees C",
        "next_file": "blog-details-8.html",
        "next_title": "Millets: jowar, bajra and ragi",
        "intro": "Finger millet (ragi) is famous for its dense nutritional profile: three times the calcium of cow's milk and rich in slowly digested polyphenols. But many home cooks find instant ragi dosas dense or rubbery. The solution is simple: a traditional fermented batter that yields lacework-crisp edges and deep umami sweetness.",
        "body_html": """
            <h2>Why fermentation is essential for ragi</h2>
            <p>Ragi contains natural phytates that bind to iron and calcium, making them harder for the body to absorb. Fermenting the batter overnight breaks down these phytates by over 75%, multiplying bioavailable calcium and creating gentle lactic acid that gives the dosa its irresistible tangy kick.</p>

            <h2>Ingredients (Yields 10–12 crispy dosas)</h2>
            <ul>
              <li><strong>1.5 cups Millstone Fresh Stone-Ground Ragi Flour</strong></li>
              <li><strong>0.5 cup Whole Urad Dal (skinned white lentils)</strong></li>
              <li><strong>0.5 cup Poha (flattened rice flakes) or raw idli rice</strong></li>
              <li><strong>0.5 tsp Fenugreek seeds (methi)</strong></li>
              <li><strong>1 tsp Rock salt</strong></li>
              <li><strong>Water as needed for soaking and grinding</strong></li>
              <li><strong>Cold-pressed sesame oil or ghee for cooking</strong></li>
            </ul>

            <h2>Step-by-step preparation</h2>
            <ol>
              <li><strong>Soak lentils (4 hours):</strong> Rinse urad dal and fenugreek seeds together in clean water. Soak for 4 hours. Soak poha separately for 30 minutes.</li>
              <li><strong>Grind to fluffy batter:</strong> Grind the urad dal and poha with cold water until airy, frothy and white like whipped cream.</li>
              <li><strong>Fold in the ragi flour:</strong> Whisk the stone-ground ragi flour into the whipped dal batter using your hand. Hand contact introduces beneficial native lactobacilli that accelerate healthy fermentation.</li>
              <li><strong>Ferment overnight (8–10 hours):</strong> Cover loosely and keep in a warm corner (26–30 °C). In winter, keep inside an oven with the pilot light on. The batter will rise and become aerated with tiny bubbles.</li>
              <li><strong>Season & Thin:</strong> Stir in salt and add just enough water until the batter flows like thick pancake batter.</li>
            </ol>

            <blockquote>Pour the batter onto a screaming-hot seasoned cast iron tawa, swirl quickly from inside out, and swirl cold-pressed gingelly oil around the perimeter.</blockquote>

            <h2>The cooking technique for paper-thin crispness</h2>
            <p>Heat a cast iron tawa until very hot. Wipe with half an onion dipped in oil. Pour a ladle of batter in the center and quickly swirl outward in concentric circles. Drizzle sesame oil around the edges and over the center. Cook on medium-high until the underside turns a deep ruby chocolate-brown and lifts cleanly from the pan without tearing.</p>
            <p>Serve immediately alongside fresh coconut chutney and spicy tomato gun-powder podi.</p>
        """
    },
    {
        "id": 8,
        "file": "blog-details-8.html",
        "title_head": "Millets: Jowar, Bajra & Ragi — Millstone & Co.",
        "desc_head": "Which millet suits which dish, how much to blend with whole wheat, and how to prevent dry crumbly rotis with hot-water kneading.",
        "heading": "Millets for beginners: jowar, bajra and ragi",
        "category": "Nutrition",
        "date": "15 Aug 2026",
        "read_time": "7 min read",
        "author": "Noa Levi",
        "role": "Grain Sourcing & Nutrition Lead",
        "initials": "NL",
        "color1": "#5b7c4b",
        "color2": "#2f4e22",
        "image": "assets/images/photo-023.jpg",
        "image_alt": "A close-up view of wheat grains on a wooden spoon with wheat stalks on a light background.",
        "caption": "From left to right: pearl millet (bajra), sorghum (jowar), and finger millet (ragi) in their unpolished whole-grain state.",
        "author_bio": "Noa heads grain nutrition research at Millstone, helping families reintroduce ancient climate-resilient millets into their daily meals.",
        "prev_file": "blog-details-7.html",
        "prev_title": "Crisp ragi dosa with a fermented batter",
        "next_file": "blog-details-9.html",
        "next_title": "Meet the team behind Granary Lane",
        "intro": "Millets are ancient, climate-resilient supergrains that have fed the Indian subcontinent for more than 5,000 years. They require 70% less water than rice or wheat and boast remarkable glycemic stability. Yet many beginners struggle because millets contain zero gluten. Here is your practical guide to cooking with jowar, bajra, and ragi.",
        "body_html": """
            <h2>The three staple millets: profile & seasonality</h2>
            <div class="row g-3 my-3">
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-light-subtle border">
                  <h3 class="h6 fw-bold text-primary">Jowar (Sorghum)</h3>
                  <p class="small text-muted mb-0"><strong>Season:</strong> All year round.<br><strong>Taste:</strong> Mild, neutral, slightly nutty.<br><strong>Best for:</strong> Daily bhakris, parathas, porridge.<br><strong>Key nutrient:</strong> High dietary fibre and complex copper.</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-light-subtle border">
                  <h3 class="h6 fw-bold text-primary">Bajra (Pearl Millet)</h3>
                  <p class="small text-muted mb-0"><strong>Season:</strong> Autumn & Winter (warming grain).<br><strong>Taste:</strong> Earthy, robust, slightly sweet.<br><strong>Best for:</strong> Winter rotlas with jaggery and butter.<br><strong>Key nutrient:</strong> Rich in bioavailable iron and zinc.</p>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-light-subtle border">
                  <h3 class="h6 fw-bold text-primary">Ragi (Finger Millet)</h3>
                  <p class="small text-muted mb-0"><strong>Season:</strong> All year round.<br><strong>Taste:</strong> Deep earthy cocoa-like aroma.<br><strong>Best for:</strong> Dosas, mudde, malt drinks, cookies.<br><strong>Key nutrient:</strong> Supreme calcium (344 mg/100g).</p>
                </div>
              </div>
            </div>

            <h2>How to blend millets with Sharbati wheat</h2>
            <p>If your household is new to millets, do not immediately switch to 100% millet rotis; the lack of gluten will frustrate novice kneaders. We recommend progressive blending:</p>
            <ul>
              <li><strong>Beginner (Week 1–2):</strong> 80% Sharbati Whole Wheat + 20% Jowar or Ragi. Rotis roll almost identically to regular atta.</li>
              <li><strong>Intermediate (Week 3–4):</strong> 60% Sharbati Whole Wheat + 40% Millet blend. Adds noticeable nutty depth and darker colour.</li>
              <li><strong>Advanced (Millet Master):</strong> 100% single millet bhakri using the hot water boiling method.</li>
            </ul>

            <blockquote>The secret to 100% millet dough is boiling water: hot water pre-gelatinizes the millet starches, acting as an edible natural glue.</blockquote>

            <h2>The hot water method for 100% millet rotis</h2>
            <p>To roll pure jowar or bajra bhakris without cracking:</p>
            <ol>
              <li>Boil 1 cup of water in a pan with a pinch of salt.</li>
              <li>Lower flame and pour in 1 cup of fresh stone-ground millet flour. Stir vigorously with a wooden spoon until a wet ball forms.</li>
              <li>Turn off flame, cover with lid and let steam for 5 minutes.</li>
              <li>Tip the warm dough onto a plate and knead with wet palms for 2 minutes into a smooth dough.</li>
              <li>Pat between palms or roll gently between two parchment sheets. It will puff like a regular roti!</li>
            </ol>

            <h2>Why fresh milling matters twice as much for millets</h2>
            <p>Millets have exposed outer fats that oxidize much faster than wheat once ground. Commercial packaged millet flours that sit on retail shelves for months often taste unpleasantly bitter. At Millstone, we stone-grind millets in small 20 kg lots to order, ensuring sweet, fragrant flavour every time.</p>
        """
    },
    {
        "id": 9,
        "file": "blog-details-9.html",
        "title_head": "Meet the Millstone Team — Millstone & Co.",
        "desc_head": "Five people, two pairs of granite stones, and 3,200+ local families. Introducing the artisans behind Millstone & Co. in Granary Lane.",
        "heading": "Meet the team behind Granary Lane",
        "category": "Company news",
        "date": "6 Aug 2026",
        "read_time": "4 min read",
        "author": "Harold Becker",
        "role": "Founder & Master Miller",
        "initials": "HB",
        "color1": "#8b5a2b",
        "color2": "#4a2f13",
        "image": "assets/images/photo-024.jpg",
        "image_alt": "Two bakers prepare traditional Middle Eastern bread in a brick oven.",
        "caption": "Harold Becker and the milling crew inspecting stone alignment before the morning grind at Granary Lane.",
        "author_bio": "Harold founded Millstone & Co. with a single chakki unit in 1987. Nearly four decades later, he continues to work the morning milling shift alongside Meera.",
        "prev_file": "blog-details-8.html",
        "prev_title": "Millets: jowar, bajra and ragi",
        "next_file": "blog-details.html",
        "next_title": "Why we still dress our millstones by hand",
        "intro": "When people discover Millstone & Co., they often assume we are either a hundred-person corporate food brand or a tiny hobby workshop. In reality, we are five dedicated people working out of a historic brick mill on Granary Lane, grinding grain every morning for more than 3,200 neighborhood households.",
        "body_html": """
            <h2>The five faces of Granary Lane</h2>
            <p>Every bag of flour that leaves our doorstep has been touched, checked, and approved by our tight-knit team:</p>

            <div class="row g-4 my-3">
              <div class="col-md-6">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <div class="d-flex align-items-center gap-3 mb-2">
                    <span class="avatar avatar-md" style="--c1:#8b5a2b;--c2:#4a2f13">HB</span>
                    <div>
                      <h3 class="h6 fw-bold mb-0">Harold Becker</h3>
                      <small class="text-muted">Founder & Master Miller</small>
                    </div>
                  </div>
                  <p class="small text-muted mb-0">Started the mill 39 years ago. Harold still manages stone calibration, granite redressing schedules, and partner farm relationships.</p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <div class="d-flex align-items-center gap-3 mb-2">
                    <span class="avatar avatar-md" style="--c1:#c9a24b;--c2:#7a5a1e">MK</span>
                    <div>
                      <h3 class="h6 fw-bold mb-0">Meera Kapoor</h3>
                      <small class="text-muted">Head Miller</small>
                    </div>
                  </div>
                  <p class="small text-muted mb-0">With us since 2009. Meera oversees every morning grinding run, monitors infrared temperature monitors, and tests flour hydration.</p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <div class="d-flex align-items-center gap-3 mb-2">
                    <span class="avatar avatar-md" style="--c1:#5b7c4b;--c2:#2f4e22">NL</span>
                    <div>
                      <h3 class="h6 fw-bold mb-0">Noa Levi</h3>
                      <small class="text-muted">Grain Sourcing & Nutrition</small>
                    </div>
                  </div>
                  <p class="small text-muted mb-0">Spends harvest season in Sehore and Maharashtra checking soil microbiology, moisture specs, and fair farmer compensation.</p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="p-3 border rounded-3 bg-light-subtle h-100">
                  <div class="d-flex align-items-center gap-3 mb-2">
                    <span class="avatar avatar-md" style="--c1:#3b6e8c;--c2:#1d4257">DO</span>
                    <div>
                      <h3 class="h6 fw-bold mb-0">Daniel Okafor</h3>
                      <small class="text-muted">Logistics & Operations</small>
                    </div>
                  </div>
                  <p class="small text-muted mb-0">Coordinates our temperature-controlled electric delivery vans so every bag arrives at customer homes within 24 hours of grinding.</p>
                </div>
              </div>
            </div>

            <blockquote>We don't want to become a nationwide mega-conglomerate. We want to be your family's trusted neighborhood flour miller for the next forty years.</blockquote>

            <h2>A morning at the mill</h2>
            <p>Our day starts at 5:00 am. Harold and Meera check the morning humidity and inspect the grain hoppers. By 5:30 am, the low, soothing hum of the heavy granite stones fills Granary Lane. As fresh flour streams into the cooling bins, the aroma of warm toasted wheat drifts down the street.</p>
            <p>By 8:00 am, Daniel has routes mapped and electric vans loaded. By noon, the flour that was a whole wheat kernel at dawn is already in your kitchen, waiting to be kneaded for family dinner.</p>

            <h2>Come say hello on Granary Lane</h2>
            <p>Our mill doors are open to visitors Monday through Saturday, from 7:00 am to 7:00 pm. Whether you want to pick up a warm 5 kg bag directly or watch Meera dress the stone furrows, the kettle is always on.</p>
        """
    }
]

def generate_blog_page(post):
    file_name = post["file"]
    
    # Calculate three related posts
    related_candidates = [p for p in POSTS if p["id"] != post["id"]]
    related = related_candidates[:3]

    content = f"""<!DOCTYPE html>
<html lang="en" dir="ltr" data-bs-theme="light">
<head>
<!-- @head {{"title": "{post['title_head']}", "description": "{post['desc_head']}", "file": "{file_name}"}} -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{post['title_head']}</title>
<meta name="description" content="{post['desc_head']}">
<link rel="canonical" href="https://www.example.com/millstone/{file_name}">
<meta property="og:title" content="{post['title_head']}">
<meta property="og:description" content="{post['desc_head']}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.example.com/millstone/{file_name}">
<meta property="og:image" content="assets/images/brand-og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" id="bs-css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="assets/css/style.css">
<script>
(function(){{
  var d=localStorage.getItem('mm-dir')||'ltr';
  var t=localStorage.getItem('mm-theme')||'light';
  document.documentElement.setAttribute('dir',d);
  document.documentElement.setAttribute('data-bs-theme',t);
  var c=document.getElementById('bs-css');
  if(c){{
    c.href=d==='rtl'?'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css':'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css';
  }}
}})();
</script>
<!-- @head:end -->
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<!-- @header {{"nav": "blog"}} -->
<!-- @header:end -->

<main id="main">

  <!-- Hero section featuring the exact card front image -->
  <section class="page-hero article-hero" style="background-image: linear-gradient(rgba(42, 26, 13, .75), rgba(42, 26, 13, .75)), url('{post['image']}');" aria-labelledby="article-title">
    <div class="container-xxl">
      <nav aria-label="Breadcrumb" class="mb-3">
        <a href="blog.html" class="hero-back-link text-decoration-none fw-semibold">
          <i class="bi bi-arrow-left" aria-hidden="true"></i> Back to all articles
        </a>
      </nav>
      <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
        <span class="badge-soft">{post['category']}</span>
        <span class="text-muted d-none d-sm-inline">•</span>
        <span class="meta-item"><i class="bi bi-calendar3 me-1" aria-hidden="true"></i>{post['date']}</span>
        <span class="text-muted d-none d-sm-inline">•</span>
        <span class="meta-item"><i class="bi bi-clock me-1" aria-hidden="true"></i>{post['read_time']}</span>
      </div>
      <h1 id="article-title" class="h-section mb-3">{post['heading']}</h1>
      <div class="meta d-flex align-items-center gap-3 mt-4 pt-3 border-top border-secondary-subtle">
        <span class="avatar avatar-md" style="--c1:{post['color1']};--c2:{post['color2']}" aria-hidden="true">{post['initials']}</span>
        <div>
          <div class="fw-bold">{post['author']}</div>
          <small class="text-muted">{post['role']}</small>
        </div>
      </div>
    </div>
  </section>

  <!-- Article Body and Sidebar -->
  <section class="section-sm" aria-label="Article content and blog sidebar">
    <div class="container-xxl">
      <div class="row g-5">

        <div class="col-lg-8">
          <article class="article" aria-labelledby="article-title">
            <p class="lead-lg">{post['intro']}</p>

            <!-- Prominently showcase the exact front container image as the featured photo -->
            <figure class="featured-article-figure mb-5">
              <div class="ph ph-wide rounded-4 overflow-hidden shadow-sm" role="img" aria-label="{post['image_alt']}">
                <img class="ph-photo w-100 object-fit-cover" src="{post['image']}" alt="{post['image_alt']}" loading="eager" style="max-height: 500px;">
              </div>
              <figcaption class="meta mt-2 text-center text-muted">{post['caption']}</figcaption>
            </figure>

            {post['body_html']}
          </article>

          <!-- Share section -->
          <div class="d-flex flex-wrap align-items-center gap-2 mt-5 pt-3 border-top">
            <strong class="me-2">Share this story:</strong>
            <button type="button" class="icon-btn" aria-label="Share on Facebook" data-demo-toast="Demo only: sharing is not connected."><i class="bi bi-facebook" aria-hidden="true"></i></button>
            <button type="button" class="icon-btn" aria-label="Share on WhatsApp" data-demo-toast="Demo only: sharing is not connected."><i class="bi bi-whatsapp" aria-hidden="true"></i></button>
            <button type="button" class="icon-btn" aria-label="Copy link to this story" data-demo-toast="Demo only: link not copied."><i class="bi bi-link-45deg" aria-hidden="true"></i></button>
          </div>

          <!-- Author Bio -->
          <aside class="mm-card p-4 mt-4" aria-labelledby="author-title">
            <div class="d-flex gap-3 align-items-start">
              <span class="avatar avatar-lg flex-shrink-0" style="--c1:{post['color1']};--c2:{post['color2']}" aria-hidden="true">{post['initials']}</span>
              <div>
                <h2 id="author-title" class="h5 mb-1">About {post['author']}</h2>
                <p class="text-muted mb-0">{post['author_bio']}</p>
              </div>
            </div>
          </aside>

          <!-- Next & Previous Navigation Links -->
          <nav class="row g-3 mt-4" aria-label="Previous and next posts">
            <div class="col-sm-6">
              <a class="mm-card mm-card-hover p-3 d-block text-decoration-none h-100" href="{post['prev_file']}">
                <span class="meta d-block mb-1"><i class="bi bi-arrow-left" aria-hidden="true"></i> Previous Article</span>
                <strong class="text-body">{post['prev_title']}</strong>
              </a>
            </div>
            <div class="col-sm-6">
              <a class="mm-card mm-card-hover p-3 d-block text-decoration-none h-100" href="{post['next_file']}">
                <span class="meta d-block mb-1">Next Article <i class="bi bi-arrow-right" aria-hidden="true"></i></span>
                <strong class="text-body">{post['next_title']}</strong>
              </a>
            </div>
          </nav>
        </div>

        <!-- Sidebar -->
        <div class="col-lg-4">
          <aside aria-label="Blog sidebar" class="d-grid gap-4">

            <div class="mm-card p-4">
              <h2 class="h5 mb-3">Search the blog</h2>
              <form role="search" data-demo-form data-demo-message="Search filters available on the main blog page." aria-label="Search posts">
                <label for="side-search" class="visually-hidden">Search posts</label>
                <div class="input-icon"><i class="bi bi-search" aria-hidden="true"></i><input type="search" id="side-search" class="form-control" placeholder="Search posts" required autocomplete="off"></div>
              </form>
              <p class="demo-note mt-2 mb-0">Front-end demo — search is active on the <a href="blog.html">main blog</a>.</p>
            </div>

            <div class="mm-card p-4">
              <h2 class="h5 mb-3">Categories</h2>
              <ul class="list-clean">
                <li class="d-flex justify-content-between py-1"><a href="blog.html">Milling</a><span class="text-muted">2</span></li>
                <li class="d-flex justify-content-between py-1"><a href="blog.html">Nutrition</a><span class="text-muted">2</span></li>
                <li class="d-flex justify-content-between py-1"><a href="blog.html">Recipes</a><span class="text-muted">2</span></li>
                <li class="d-flex justify-content-between py-1"><a href="blog.html">Sourcing</a><span class="text-muted">1</span></li>
                <li class="d-flex justify-content-between py-1"><a href="blog.html">Company news</a><span class="text-muted">2</span></li>
              </ul>
            </div>

            <div class="mm-card p-4">
              <h2 class="h5 mb-3">Recent stories</h2>
              <ul class="list-clean d-grid gap-3">
                <li class="d-flex gap-3 align-items-center">
                  <a href="blog-details-3.html" class="flex-shrink-0" aria-label="Read Soft phulka rotis">
                    <img src="assets/images/photo-067.jpg" alt="Phulka rotis on tawa" class="rounded object-fit-cover" width="60" height="60" loading="lazy">
                  </a>
                  <div>
                    <a href="blog-details-3.html" class="fw-semibold text-decoration-none">Soft phulka rotis: 70% hydration</a>
                    <span class="meta d-block">28 Sep 2026</span>
                  </div>
                </li>
                <li class="d-flex gap-3 align-items-center">
                  <a href="blog-details-4.html" class="flex-shrink-0" aria-label="Read Visiting farms">
                    <img src="assets/images/photo-019.jpg" alt="Wheat field landscape" class="rounded object-fit-cover" width="60" height="60" loading="lazy">
                  </a>
                  <div>
                    <a href="blog-details-4.html" class="fw-semibold text-decoration-none">Visiting farms behind our wheat</a>
                    <span class="meta d-block">19 Sep 2026</span>
                  </div>
                </li>
                <li class="d-flex gap-3 align-items-center">
                  <a href="blog-details-6.html" class="flex-shrink-0" aria-label="Read Keeping flour below 40C">
                    <img src="assets/images/photo-051.jpg" alt="Fresh flour container" class="rounded object-fit-cover" width="60" height="60" loading="lazy">
                  </a>
                  <div>
                    <a href="blog-details-6.html" class="fw-semibold text-decoration-none">How we keep flour below 40 °C</a>
                    <span class="meta d-block">2 Sep 2026</span>
                  </div>
                </li>
              </ul>
            </div>

            <div class="mm-card p-4">
              <h2 class="h5 mb-3">Tags</h2>
              <div class="d-flex flex-wrap gap-2">
                <a class="tag" href="blog.html">Sharbati</a><a class="tag" href="blog.html">Chakki</a><a class="tag" href="blog.html">Whole grain</a><a class="tag" href="blog.html">Millets</a><a class="tag" href="blog.html">Rotis</a><a class="tag" href="blog.html">Stone cold</a>
              </div>
            </div>

            <div class="mm-card p-4 text-center">
              <span class="icon-tile mb-3"><i class="bi bi-truck" aria-hidden="true"></i></span>
              <h2 class="h5">Fresh atta at your door</h2>
              <p class="text-muted small">Stone-ground this morning, delivered fresh tomorrow. Free delivery on every subscription plan.</p>
              <a class="btn btn-primary w-100" href="delivery-plans.html">Explore delivery plans</a>
            </div>

          </aside>
        </div>

      </div>
    </div>
  </section>

  <!-- Related stories section -->
  <section class="section section-alt" aria-labelledby="related-title">
    <div class="container-xxl">
      <div class="d-flex justify-content-between align-items-end mb-4">
        <div>
          <span class="eyebrow mb-2">Continue reading</span>
          <h2 id="related-title" class="h-section mb-0">More stories from Granary Lane</h2>
        </div>
        <a href="blog.html" class="btn btn-outline-primary d-none d-md-inline-flex">All articles</a>
      </div>
      <div class="row g-4">
"""
    for r in related:
        content += f"""        <div class="col-md-4">
          <article class="mm-card mm-card-hover blog-card h-100">
            <a href="{r['file']}" class="d-block" aria-label="Read article: {r['heading']}">
              <div class="ph ph-wide rounded-top overflow-hidden" role="img" aria-label="{r['image_alt']}">
                <img class="ph-photo" src="{r['image']}" alt="{r['image_alt']}" loading="lazy" decoding="async">
              </div>
            </a>
            <div class="card-body">
              <p class="meta mb-2"><span class="badge-soft">{r['category']}</span><span>{r['date']}</span><span>{r['read_time']}</span></p>
              <h3 class="h5"><a href="{r['file']}">{r['heading']}</a></h3>
              <p class="meta mt-auto mb-0"><i class="bi bi-person" aria-hidden="true"></i> By {r['author']}</p>
            </div>
          </article>
        </div>
"""

    content += f"""      </div>
    </div>
  </section>

  <!-- Newsletter callout -->
  <section class="section-sm" aria-labelledby="news-title">
    <div class="container-xxl">
      <div class="mm-card p-4 p-lg-5" data-reveal>
        <div class="row g-4 align-items-center">
          <div class="col-lg-6">
            <span class="eyebrow mb-3">Newsletter</span>
            <h2 id="news-title" class="h-section mb-2">One email a month, fresh from the mill.</h2>
            <p class="text-muted mb-0">Seasonal grain news, a new atta recipe and first notice of delivery changes. No spam, unsubscribe any time.</p>
          </div>
          <div class="col-lg-6">
            <form data-demo-form data-demo-message="Thanks!" aria-label="Newsletter sign-up" class="d-flex flex-column flex-sm-row gap-2">
              <label for="detail-news-email" class="visually-hidden">Email address</label>
              <input type="email" id="detail-news-email" class="form-control form-control-lg" placeholder="you@example.com" required autocomplete="email">
              <button type="submit" class="btn btn-primary btn-lg">Subscribe</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
<!-- @footer -->
<!-- @footer:end -->
<!-- @scripts -->
<!-- @scripts:end -->
</body>
</html>
"""
    target_path = ROOT / file_name
    target_path.write_text(content, encoding="utf-8")
    print(f"Generated {file_name}")

if __name__ == "__main__":
    for post in POSTS:
        generate_blog_page(post)
    print("All 9 blog pages generated successfully.")
