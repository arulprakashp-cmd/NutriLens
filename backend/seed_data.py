"""
Seed data for Nutrients Story app
Contains all topics (Protein, Carbs, Fats) with their cards
"""

TOPICS_DATA = [
    {
        "topic_id": "topic_protein",
        "key": "protein",
        "title": "The Protein Story",
        "subtitle": "Why it matters · every body · every age",
        "icon_name": "fitness",  # Ionicons
        "emoji": "💪",
        "background_color": "#EDE8DF",
        "description": "9 cards · Cell repair, amino acids, daily targets & Indian sources",
        "card_count": 9,
        "order": 1,
        "cards": [
            {
                "card_id": "protein_01",
                "number": "01",
                "label": "Reality Check",
                "icon": "⚠️",
                "title": "India Has a Hidden Protein Gap",
                "order": 1,
                "content": {
                    "type": "stats",
                    "body": "Most Indians eat enough calories — yet remain protein deficient. We fill our plates with carbs, but the body's building blocks are missing.",
                    "stats": [
                        {"value": "73%", "label": "Indians consume below recommended protein levels daily"},
                        {"value": "0.8g", "label": "Minimum protein per kg of body weight per day"},
                        {"value": "1.2g", "label": "Optimal per kg for active adults & healthy aging"}
                    ]
                }
            },
            {
                "card_id": "protein_02",
                "number": "02",
                "label": "Why Protein?",
                "icon": "🧱",
                "title": "Your Body's Master Builder",
                "order": 2,
                "content": {
                    "type": "benefits",
                    "body": "Protein is needed at every stage of life — not just for athletes. It builds, repairs, and sustains you daily.",
                    "benefits": [
                        {"icon": "👶", "title": "Children", "description": "Fuels growth, brain development & sharp cognitive function"},
                        {"icon": "💪", "title": "Adults", "description": "Repairs cells, maintains muscle mass & sustains daily energy"},
                        {"icon": "✨", "title": "Women", "description": "Produces collagen → glowing skin, strong hair & nails"},
                        {"icon": "🧓", "title": "Seniors", "description": "Prevents muscle loss (sarcopenia) & supports bone density"}
                    ]
                }
            },
            {
                "card_id": "protein_03",
                "number": "03",
                "label": "Anti-Aging & Cell Repair",
                "icon": "⏳",
                "title": "How Protein Fights Time",
                "order": 3,
                "content": {
                    "type": "process",
                    "body": "At the cellular level, protein is your body's repair crew — working 24/7 to keep you younger, stronger & healthier.",
                    "steps": [
                        {"number": 1, "title": "Cell Repair & Renewal", "description": "Amino acids rebuild damaged cells & create healthy new ones — slowing tissue degradation"},
                        {"number": 2, "title": "Collagen Production", "description": "Keeps skin firm, joints supple & gut lining strong — nature's anti-aging protein"},
                        {"number": 3, "title": "Enzyme & Hormone Synthesis", "description": "Proteins form enzymes that control digestion, immunity & hormones like insulin"},
                        {"number": 4, "title": "Muscle Preservation", "description": "Prevents age-related muscle loss — keeping you mobile, strong & independent"}
                    ]
                }
            },
            {
                "card_id": "protein_04",
                "number": "04",
                "label": "Amino Acids",
                "icon": "🔬",
                "title": "20 Building Blocks. 9 You Must Eat.",
                "order": 4,
                "content": {
                    "type": "amino_acids",
                    "body": "Proteins are chains of 20 amino acids. Your body makes 11 — but 9 essential ones must come from food every day.",
                    "essential": 9,
                    "non_essential": 11,
                    "note": "💡 Complete proteins contain all 9 essential amino acids. Animal foods are naturally complete. Most plant foods are incomplete — they may lack one or more essential amino acids. Combine foods like rice + dal or roti + curd to get the full spectrum."
                }
            },
            {
                "card_id": "protein_05",
                "number": "05",
                "label": "Protein vs Calories",
                "icon": "⚖️",
                "title": "Not All Calories Are Equal",
                "order": 5,
                "content": {
                    "type": "comparison",
                    "body": "1g of protein = 4 kcal — same as carbs. But protein does far more than just fuel you.",
                    "macros": [
                        {"name": "Protein", "kcal": 4, "color": "#C8441A"},
                        {"name": "Fat", "kcal": 9, "color": "#8B6914"},
                        {"name": "Carbohydrates", "kcal": 4, "color": "#6B8F71"}
                    ],
                    "callout": "🔥 Protein keeps you fuller longer, boosts metabolism & burns more calories during digestion — your smartest macronutrient. Eating 30g protein at breakfast can cut cravings all day."
                }
            },
            {
                "card_id": "protein_06",
                "number": "06",
                "label": "Your Protein Plan",
                "icon": "🍽️",
                "title": "How Much & From Where?",
                "order": 6,
                "content": {
                    "type": "protein_plan",
                    "body": "Recommended protein intake varies by age and activity level.",
                    "intake": [
                        {"emoji": "🧒", "value": "1.5g", "label": "per kg · Kids"},
                        {"emoji": "🏃", "value": "1.2g", "label": "per kg · Active Adults"},
                        {"emoji": "🤰", "value": "1.5g", "label": "per kg · Pregnant"},
                        {"emoji": "🧓", "value": "1.2g", "label": "per kg · Seniors 60+"}
                    ],
                    "sources": {
                        "complete": {
                            "label": "High-Quality Complete Protein",
                            "badge": "All 9 Amino Acids",
                            "foods": ["🥚 Eggs", "🍗 Chicken", "🐟 Fish", "🧆 Paneer", "🫙 Curd/Yogurt", "🥛 Milk"]
                        },
                        "plant": {
                            "label": "Plant Protein",
                            "badge": "Combine for Full Profile",
                            "foods": ["🫘 Dal/Lentils", "🌰 Soya Chunks", "🥜 Peanuts", "🫛 Chickpeas", "🌾 Quinoa*"],
                            "note": "⚠️ Most plant proteins are incomplete — they lack one or more essential amino acids. *Quinoa is a rare complete plant protein. Combine rice + dal or roti + curd to get the full amino acid profile."
                        }
                    }
                }
            },
            {
                "card_id": "protein_07",
                "number": "07",
                "label": "Protein Per 100g",
                "icon": "📊",
                "title": "How Much Protein Is In Your Food?",
                "order": 7,
                "content": {
                    "type": "protein_bars",
                    "body": "Gram for gram, not all protein foods are equal. Here's what 100g of common foods actually deliver.",
                    "categories": [
                        {
                            "name": "Animal Protein",
                            "emoji": "🥩",
                            "foods": [
                                {"emoji": "🐔", "name": "Chicken Breast", "protein": 31, "note": "Lean, complete, highest protein density"},
                                {"emoji": "🐟", "name": "Tuna / Rohu Fish", "protein": 26, "note": "Rich in omega-3 + complete protein"},
                                {"emoji": "🧆", "name": "Paneer", "protein": 18, "note": "Good complete protein, higher in fat"},
                                {"emoji": "🫙", "name": "Curd / Yogurt", "protein": 10, "note": "Easy daily protein + gut-friendly probiotics"},
                                {"emoji": "🥚", "name": "1 Whole Egg (~55g)", "protein": 7, "note": "Gold standard — perfect amino acid profile. 3 eggs = ~19g"}
                            ]
                        },
                        {
                            "name": "Plant Protein",
                            "emoji": "🌿",
                            "foods": [
                                {"emoji": "🌰", "name": "Soya Chunks (dry)", "protein": 52, "note": "Highest plant protein — nearly complete"},
                                {"emoji": "🥜", "name": "Peanuts", "protein": 26, "note": "High protein but also high in fat"},
                                {"emoji": "🫘", "name": "Lentils / Dal (cooked)", "protein": 9, "note": "Incomplete — pair with rice for full profile"}
                            ]
                        },
                        {
                            "name": "Nuts & Dry Fruits",
                            "emoji": "🌰",
                            "foods": [
                                {"emoji": "🌰", "name": "Almonds", "protein": 21, "note": "Also rich in Vitamin E, healthy fats & magnesium"},
                                {"emoji": "💚", "name": "Pistachios (Pista)", "protein": 20, "note": "Highest protein among common nuts + rich in B6"},
                                {"emoji": "🥜", "name": "Cashews (Kaju)", "protein": 18, "note": "Good protein but higher in carbs than other nuts"},
                                {"emoji": "🪨", "name": "Walnuts (Akhrot)", "protein": 15, "note": "Lower protein but excellent omega-3 & brain health"}
                            ]
                        }
                    ]
                }
            },
            {
                "card_id": "protein_08",
                "number": "08",
                "label": "Daily Meal Plan",
                "icon": "🗓️",
                "title": "72g Protein Day for a 60kg Person",
                "order": 8,
                "content": {
                    "type": "meal_plan",
                    "body": "Target: 60 × 1.2 = 72g protein/day. Here's how a real Indian day can hit that goal deliciously.",
                    "meals": [
                        {
                            "time": "Breakfast",
                            "icon": "🌅",
                            "total": "~22g protein",
                            "items": [
                                {"food": "🥚 3 Eggs / ~150g (scrambled / boiled)", "protein": 19},
                                {"food": "🥛 1 glass milk (200ml)", "protein": 7},
                                {"food": "🫓 2 whole wheat rotis", "protein": 6, "muted": True}
                            ]
                        },
                        {
                            "time": "Lunch",
                            "icon": "☀️",
                            "total": "~24g protein",
                            "items": [
                                {"food": "🍗 100g chicken curry", "protein": 31},
                                {"food": "🫘 1 katori dal", "protein": 9},
                                {"food": "🍚 1 cup cooked rice + sabzi", "protein": 4, "muted": True}
                            ]
                        },
                        {
                            "time": "Evening Snack",
                            "icon": "🌤️",
                            "total": "~12g protein",
                            "items": [
                                {"food": "🫙 1 bowl hung curd / yogurt", "protein": 10},
                                {"food": "🥜 Small handful peanuts (30g)", "protein": 8}
                            ]
                        },
                        {
                            "time": "Dinner",
                            "icon": "🌙",
                            "total": "~18g protein",
                            "items": [
                                {"food": "🧆 100g paneer sabzi", "protein": 18},
                                {"food": "🌰 Soya chunks curry (50g dry)", "protein": 26},
                                {"food": "🫓 2 rotis + salad", "protein": 6, "muted": True}
                            ]
                        }
                    ],
                    "daily_total": "~76g protein ✓"
                }
            },
            {
                "card_id": "protein_09",
                "number": "09",
                "label": "Summary",
                "icon": "✅",
                "title": "Your Protein Cheat Sheet",
                "order": 9,
                "content": {
                    "type": "summary",
                    "takeaways": [
                        "Protein is the body's master builder — muscles, skin, hormones & immunity all depend on it",
                        "73% of Indians are protein deficient despite eating enough calories",
                        "9 essential amino acids must come from food — your body cannot make them",
                        "Animal proteins are complete. Most plant proteins are incomplete — combine wisely",
                        "Protein fights aging — collagen, cell repair & muscle preservation all need protein daily",
                        "1g protein = 4 kcal but it keeps you fuller, boosts metabolism & builds — not just fuels"
                    ],
                    "targets": [
                        {"who": "🧒 Kids", "amount": "1.5g / kg"},
                        {"who": "🏃 Active Adults", "amount": "1.2g / kg"},
                        {"who": "🤰 Pregnant", "amount": "1.5g / kg"},
                        {"who": "🧓 Seniors 60+", "amount": "1.2g / kg"},
                        {"who": "🪑 Sedentary Adult", "amount": "0.8g / kg"}
                    ],
                    "checklist": [
                        "Calculate your daily protein target (body weight × 1.2)",
                        "Add a protein source to every meal — not just dinner",
                        "Start breakfast with 20–30g protein (eggs, curd, milk)",
                        "If vegetarian, combine dal + rice or roti + curd daily",
                        "Use nuts & curd as protein-rich snacks instead of biscuits",
                        "Track protein for 1 week — most people are shocked how low it is"
                    ]
                }
            }
        ]
    },
    {
        "topic_id": "topic_carbs",
        "key": "carbs",
        "title": "The Carbs Story",
        "subtitle": "Friend or foe · the truth about carbohydrates",
        "icon_name": "nutrition",  # Ionicons
        "emoji": "🌾",
        "background_color": "#EDE6D6",
        "description": "12 cards · GI index, millet myth, sugar truth & smart swaps",
        "card_count": 12,
        "order": 2,
        "cards": [
            {
                "card_id": "carbs_01",
                "number": "01",
                "label": "Reality Check",
                "icon": "🍚",
                "title": "India's Carb Overload Problem",
                "order": 1,
                "content": {
                    "type": "stats",
                    "body": "We eat more carbs than almost any country — but mostly the wrong kind. White rice, maida & sugar dominate every meal. The result? A nation of energy crashes, expanding waistlines & exploding diabetes rates.",
                    "stats": [
                        {"value": "70%", "label": "of Indian calories come from carbs daily"},
                        {"value": "#1", "label": "India leads globally in diabetes cases"},
                        {"value": "101M", "label": "Indians living with Type 2 diabetes — diet is the primary driver"}
                    ]
                }
            },
            {
                "card_id": "carbs_02",
                "number": "02",
                "label": "Why We Need Carbs",
                "icon": "⚡",
                "title": "Carbs Are Not the Enemy",
                "order": 2,
                "content": {
                    "type": "benefits",
                    "body": "Your body needs carbohydrates. The brain runs exclusively on glucose. The problem is never carbs — it's the type and quality of carbs you eat.",
                    "benefits": [
                        {"icon": "🧠", "title": "Brain Fuel", "description": "The brain uses glucose exclusively — it cannot run on fat or protein directly"},
                        {"icon": "💪", "title": "Muscle Power", "description": "Glycogen (stored carbs) powers every physical movement from walking to lifting"},
                        {"icon": "❤️", "title": "Organ Function", "description": "Kidneys, heart & liver all rely on glucose to function optimally"},
                        {"icon": "😊", "title": "Mood & Focus", "description": "Stable blood sugar = stable mood. Carb crashes cause irritability & brain fog"}
                    ],
                    "callout": "💡 Cutting carbs completely = fatigue, brain fog & muscle loss. The goal is smarter carbs, not zero carbs."
                }
            },
            {
                "card_id": "carbs_03",
                "number": "03",
                "label": "Good vs Bad Carbs",
                "icon": "⚖️",
                "title": "Not All Carbs Are Created Equal",
                "order": 3,
                "content": {
                    "type": "split_comparison",
                    "body": "The difference between good and bad carbs is how fast they break down and what else they bring along.",
                    "good": ["🌾 Whole grains", "🫘 Lentils & dal", "🥦 Vegetables", "🍠 Sweet potato", "🌾 Oats & millets", "🍌 Whole fruit"],
                    "bad": ["🍞 White bread", "🍚 White rice", "🍬 Sugar & sweets", "🧁 Maida / Biscuits", "🥤 Sugary drinks", "🍟 Processed snacks"],
                    "tip": "💡 Good carbs come with fibre, vitamins & minerals. Bad carbs are stripped of all nutrition — just empty calories that spike your blood sugar."
                }
            },
            {
                "card_id": "carbs_04",
                "number": "04",
                "label": "Inside Your Body",
                "icon": "🔄",
                "title": "The Refined Carb Vicious Cycle",
                "order": 4,
                "content": {
                    "type": "process",
                    "body": "Every time you eat refined carbs, this chain reaction starts — and it ends with more hunger than when you began.",
                    "steps": [
                        {"number": 1, "title": "Rapid Digestion", "description": "Refined carbs break down fast → blood glucose spikes sharply within 30 minutes"},
                        {"number": 2, "title": "Insulin Flood", "description": "Pancreas releases large insulin burst to remove excess glucose from blood"},
                        {"number": 3, "title": "Fat Storage", "description": "Excess glucose is converted to fat, especially visceral (belly) fat"},
                        {"number": 4, "title": "Blood Sugar Crash", "description": "Insulin overshoots → blood sugar drops below normal → energy crash & brain fog"},
                        {"number": 5, "title": "Hunger Returns", "description": "Low blood sugar triggers intense craving for more carbs — the cycle repeats"}
                    ],
                    "callout": "🔁 Repeat this cycle daily for years → insulin resistance → Type 2 diabetes"
                }
            },
            {
                "card_id": "carbs_05",
                "number": "05",
                "label": "Glycemic Index",
                "icon": "📈",
                "title": "The GI Scale — Speed of Blood Sugar Rise",
                "order": 5,
                "content": {
                    "type": "gi_scale",
                    "body": "Glycemic Index (GI) measures how fast a food raises blood sugar on a scale of 0–100. Lower is better.",
                    "bands": [
                        {"level": "High GI", "range": "≥70", "color": "#E07070", "description": "Fast spike, fast crash. Promotes fat storage & insulin resistance"},
                        {"level": "Medium GI", "range": "56 to 69", "color": "#F0A060", "description": "Moderate rise. Okay in small portions, better with fibre & protein"},
                        {"level": "Low GI", "range": "≤55", "color": "#5DBE7A", "description": "Slow energy release, keeps you full longer, no sugar spike"}
                    ],
                    "note": "🇮🇳 Indians are 3–4× more prone to insulin resistance than Western populations at the same BMI — making GI awareness especially critical for us."
                }
            },
            {
                "card_id": "carbs_06",
                "number": "06",
                "label": "GI of Indian Foods",
                "icon": "🚦",
                "title": "Traffic Light GI Chart",
                "order": 6,
                "content": {
                    "type": "gi_chart",
                    "body": "How fast does your daily food spike blood sugar?",
                    "foods": [
                        {"name": "🍞 White Bread/Maida", "gi": 80, "level": "high"},
                        {"name": "🥔 Potato (boiled)", "gi": 78, "level": "high"},
                        {"name": "🍚 White Rice", "gi": 76, "level": "high"},
                        {"name": "🌾 Bajra (Millet)", "gi": 71, "level": "high"},
                        {"name": "🌾 Jowar (Millet)", "gi": 70, "level": "high"},
                        {"name": "🌾 Ragi (Finger Millet)", "gi": 68, "level": "medium"},
                        {"name": "🟤 Brown Rice", "gi": 64, "level": "medium"},
                        {"name": "🫓 Roti/Chapati (atta)", "gi": 62, "level": "medium"},
                        {"name": "🌾 Oats (rolled)", "gi": 55, "level": "low"},
                        {"name": "🍌 Banana", "gi": 51, "level": "low"},
                        {"name": "🍠 Sweet Potato", "gi": 44, "level": "low"},
                        {"name": "🫘 Dal / Lentils", "gi": 32, "level": "low"},
                        {"name": "🫛 Chickpeas", "gi": 28, "level": "low"}
                    ],
                    "millet_myth": {
                        "title": "⚠️ The Millet Myth — Busted",
                        "body": "Millets are nutritionally superior to white rice — richer in fibre, iron & minerals. But their GI tells a different story.",
                        "comparison": [
                            {"name": "White Rice", "gi": 76},
                            {"name": "Bajra", "gi": 71},
                            {"name": "Jowar", "gi": 70}
                        ],
                        "note": "Switching to millets won't fix blood sugar spikes on its own. Combine with dal, vegetables & healthy fats to lower the meal's overall GI."
                    }
                }
            },
            {
                "card_id": "carbs_07",
                "number": "07",
                "label": "Carbs & Diabetes",
                "icon": "⚠️",
                "title": "Why Indians Are at Higher Risk",
                "order": 7,
                "content": {
                    "type": "benefits",
                    "body": "India is the world's diabetes capital — and diet is the primary driver. Indians have a unique metabolic vulnerability to refined carbs.",
                    "benefits": [
                        {"icon": "🧬", "title": "Genetic Insulin Resistance", "description": "Indians develop insulin resistance at lower BMI & younger age than Western populations"},
                        {"icon": "🫃", "title": "Hidden Visceral Fat", "description": "'Thin-fat' Indians — normal BMI but high belly fat — are at extreme diabetes risk"},
                        {"icon": "🍚", "title": "Rice-Dominant Diet", "description": "White rice (high GI) 2–3 times daily creates chronic blood sugar spikes"},
                        {"icon": "🏙️", "title": "Sedentary Lifestyle", "description": "Urban Indians walk less, sit more — muscles don't absorb glucose efficiently"}
                    ]
                }
            },
            {
                "card_id": "carbs_08",
                "number": "08",
                "label": "Fibre — The Secret Weapon",
                "icon": "🌿",
                "title": "Why Fibre Changes Everything",
                "order": 8,
                "content": {
                    "type": "benefits",
                    "body": "Fibre is the single most important nutrient most Indians are missing. It transforms how your body handles carbs.",
                    "benefits": [
                        {"icon": "📉", "title": "Lowers GI of Any Meal", "description": "Slows carb digestion → gentler blood sugar rise → no crash"},
                        {"icon": "🦠", "title": "Feeds Gut Bacteria", "description": "Healthy microbiome improves immunity, mood & metabolism"},
                        {"icon": "😌", "title": "Keeps You Full Longer", "description": "Prevents overeating & cravings — the best weight management tool"},
                        {"icon": "💩", "title": "Digestive Health", "description": "Prevents constipation, reduces colon cancer risk"}
                    ],
                    "callout": "🎯 Target: 25–35g fibre daily. Most Indians eat <15g."
                }
            },
            {
                "card_id": "carbs_09",
                "number": "09",
                "label": "Smart Carb Swaps",
                "icon": "🔄",
                "title": "Simple Switches, Big Impact",
                "order": 9,
                "content": {
                    "type": "swaps",
                    "body": "You don't need to eliminate carbs — just upgrade them.",
                    "swaps": [
                        {"from": "🍚 White rice (3 cups/day)", "to": "🟤 Brown rice (1.5 cups) + dal + sabzi", "impact": "GI ↓ · Fibre ↑"},
                        {"from": "🍞 White bread sandwich", "to": "🌾 Multigrain roti + paneer", "impact": "GI ↓ · Protein ↑"},
                        {"from": "🧁 Biscuits (evening snack)", "to": "🫛 Roasted chana / peanuts", "impact": "GI ↓ · Protein ↑"},
                        {"from": "🥤 Sugary drinks", "to": "🥥 Coconut water / buttermilk", "impact": "Sugar ↓ · Nutrients ↑"},
                        {"from": "🥔 Potato sabzi", "to": "🍠 Sweet potato / mixed veg", "impact": "GI ↓ · Fibre ↑"}
                    ]
                }
            },
            {
                "card_id": "carbs_10",
                "number": "10",
                "label": "Portion Control",
                "icon": "🍽️",
                "title": "How Much Carbs Per Day?",
                "order": 10,
                "content": {
                    "type": "targets",
                    "body": "Carbs should be 40–50% of total calories for most Indians.",
                    "targets": [
                        {"who": "🪑 Sedentary Adult (2000 kcal)", "amount": "~225g/day"},
                        {"who": "🏃 Active Adult (2500 kcal)", "amount": "~275g/day"},
                        {"who": "📊 % of Calories", "amount": "40–50%"},
                        {"who": "🌿 Daily Fibre", "amount": "25–35g/day"}
                    ],
                    "visual_guide": [
                        {"food": "1 cup cooked rice", "carbs": "45g"},
                        {"food": "2 whole wheat rotis", "carbs": "30g"},
                        {"food": "1 medium banana", "carbs": "27g"},
                        {"food": "1 katori dal", "carbs": "20g"}
                    ]
                }
            },
            {
                "card_id": "carbs_11",
                "number": "11",
                "label": "Sugar Truth",
                "icon": "🍯",
                "title": "All Sugars Are Nearly the Same",
                "order": 11,
                "content": {
                    "type": "sugar_comparison",
                    "body": "Brown sugar, honey & coconut sugar are all marketed as 'healthier' alternatives. Your liver doesn't care about the label.",
                    "sugars": [
                        {"name": "White Sugar", "gi": 65, "kcal": 387, "verdict": "Refined"},
                        {"name": "Brown Sugar", "gi": 64, "kcal": 380, "verdict": "Same as white"},
                        {"name": "Honey", "gi": 58, "kcal": 304, "verdict": "Still 80% sugar"},
                        {"name": "Jaggery (Gur)", "gi": 84, "kcal": 383, "verdict": "Highest GI"},
                        {"name": "Coconut Sugar", "gi": 54, "kcal": 375, "verdict": "Slightly better"},
                        {"name": "Palm Sugar", "gi": 35, "kcal": 375, "verdict": "Lowest GI"}
                    ],
                    "truth": [
                        {"point": "🍯 Honey", "detail": "Has trace enzymes & antioxidants but is 80% sugar"},
                        {"point": "🟫 Brown sugar", "detail": "Just white sugar with molasses added back — same GI"},
                        {"point": "🌴 Palm sugar", "detail": "Lowest GI (35) among common sweeteners — best choice if needed"},
                        {"point": "✅ Best swap", "detail": "Dates or fresh fruit — natural sugar with fibre to slow absorption"}
                    ]
                }
            },
            {
                "card_id": "carbs_12",
                "number": "12",
                "label": "Summary",
                "icon": "✅",
                "title": "Your Carbs Cheat Sheet",
                "order": 12,
                "content": {
                    "type": "summary",
                    "takeaways": [
                        "Carbs are essential — your brain runs exclusively on glucose. Don't cut them, choose wisely",
                        "70–80% of Indian calories come from carbs — mostly refined, which drives diabetes & obesity",
                        "Glycemic Index (GI) reveals how fast food spikes blood sugar — low GI = better choices",
                        "Millets (Bajra GI=71, Jowar GI=70) are nutritious but NOT a blood sugar solution on their own",
                        "All sugars — white, brown, honey, jaggery — are nearly identical to your body. Palm sugar has the lowest GI",
                        "Fibre is your secret weapon — it lowers the GI of any meal and feeds your gut bacteria",
                        "Indians are 3–4× more prone to insulin resistance — making smart carb choices critical"
                    ],
                    "targets": [
                        {"who": "🪑 Sedentary Adult", "amount": "~225g/day"},
                        {"who": "🏃 Active Adult", "amount": "~275g/day"},
                        {"who": "📊 % of Calories", "amount": "40–50%"},
                        {"who": "🌿 Daily Fibre", "amount": "25–35g/day"}
                    ],
                    "checklist": [
                        "Replace white rice with brown rice or reduce portion + add more dal & sabzi",
                        "Never eat carbs alone — always pair with protein or fibre to lower GI",
                        "Swap biscuits & namkeen snacks for roasted chana, peanuts or fruit",
                        "Cut sugar in tea/coffee — try palm sugar or reduce quantity gradually",
                        "Walk 10 minutes after meals — reduces blood sugar spike by up to 30%",
                        "Add more dal, vegetables & whole fruits to every meal for fibre",
                        "Check blood sugar levels once a year — many Indians are pre-diabetic unknowingly"
                    ]
                }
            }
        ]
    },
    {
        "topic_id": "topic_fats",
        "key": "fats",
        "title": "The Fat Story",
        "subtitle": "The most misunderstood macronutrient · myths busted",
        "icon_name": "water",  # Ionicons (representing oil/fat)
        "emoji": "🧈",
        "background_color": "#E8E0D0",
        "description": "13 cards · Myths busted, trans fat, cholesterol & best cooking oils",
        "card_count": 13,
        "order": 3,
        "cards": [
            {
                "card_id": "fats_01",
                "number": "01",
                "label": "The Paradox",
                "icon": "⚖️",
                "title": "Fat Was Wrongly Convicted",
                "order": 1,
                "content": {
                    "type": "timeline",
                    "body": "For 40 years, fat was declared the enemy. We removed it from everything. The result? We got sicker, fatter and more diabetic than ever before.",
                    "events": [
                        {"year": "1960s", "title": "The Big Fat Lie Begins", "description": "Ancel Keys' flawed study linked dietary fat to heart disease — ignoring data from 15 countries that didn't fit"},
                        {"year": "1980s", "title": "Low-Fat Era Launched", "description": "Governments worldwide issued dietary guidelines recommending low-fat diets. Food industry replaced fat with sugar"},
                        {"year": "1990s", "title": "Obesity Epidemic Explodes", "description": "Low-fat, high-sugar processed foods flooded markets. Obesity & diabetes rates skyrocketed globally"},
                        {"year": "2000s", "title": "Science Reverses Course", "description": "Multiple large studies found no link between dietary fat and heart disease. The original research was deeply flawed"},
                        {"year": "Today", "title": "Fat Is Rehabilitated", "description": "Sugar & refined carbs — not fat — are now identified as primary drivers of metabolic disease"}
                    ],
                    "verdict": "🏛️ Fat didn't cause the obesity epidemic. Replacing fat with sugar did."
                }
            },
            {
                "card_id": "fats_02",
                "number": "02",
                "label": "Why We Need Fat",
                "icon": "🧠",
                "title": "Your Body Cannot Function Without Fat",
                "order": 2,
                "content": {
                    "type": "fat_roles",
                    "body": "Fat is not just stored energy — it is a structural and functional necessity for every cell in your body.",
                    "macros": [
                        {"name": "Protein", "kcal": 4},
                        {"name": "Carbs", "kcal": 4},
                        {"name": "Fat", "kcal": 9}
                    ],
                    "note": "1 tbsp oil (~14g) = 126 kcal — small amounts carry big energy. Quality matters enormously.",
                    "roles": [
                        {"icon": "🧠", "title": "Brain Structure", "description": "60% of the brain is fat — DHA (omega-3) is critical for memory, focus & mental health"},
                        {"icon": "🔬", "title": "Cell Membranes", "description": "Every single cell in your body is wrapped in a fat membrane — without fat, cells cannot function"},
                        {"icon": "💊", "title": "Vitamin Absorption", "description": "Vitamins A, D, E & K are fat-soluble — they cannot be absorbed without dietary fat"},
                        {"icon": "⚗️", "title": "Hormone Production", "description": "Testosterone, oestrogen, cortisol & vitamin D are all made from cholesterol — a type of fat"}
                    ]
                }
            },
            {
                "card_id": "fats_03",
                "number": "03",
                "label": "The 4 Types of Fat",
                "icon": "🔬",
                "title": "Not All Fats Are the Same",
                "order": 3,
                "content": {
                    "type": "fat_types",
                    "body": "The type of fat you eat matters far more than the total amount. Here are the four types — from best to worst.",
                    "types": [
                        {"level": "good1", "icon": "✅", "name": "Monounsaturated (MUFA)", "description": "Heart-protective, reduces bad cholesterol, anti-inflammatory", "examples": "Olive oil, groundnut oil, avocado, almonds, cashews"},
                        {"level": "good2", "icon": "✅", "name": "Polyunsaturated (PUFA)", "description": "Essential — body cannot make them. Omega-3 & omega-6 both needed", "examples": "Fish, walnuts, flaxseed, sunflower seeds"},
                        {"level": "warn", "icon": "⚠️", "name": "Saturated Fat", "description": "Okay in moderation — not as harmful as once believed. Ghee okay sparingly", "examples": "Ghee, butter, coconut oil, red meat, full-fat dairy"},
                        {"level": "bad", "icon": "❌", "name": "Trans Fat — The Real Villain", "description": "Artificially created, directly damages arteries. No safe level of consumption", "examples": "Vanaspati, dalda, margarine, commercial biscuits, fried snacks"}
                    ]
                }
            },
            {
                "card_id": "fats_04",
                "number": "04",
                "label": "Plant Fat vs Animal Fat",
                "icon": "🥥",
                "title": "Busting the 'Plant = Good' Myth",
                "order": 4,
                "content": {
                    "type": "saturation_chart",
                    "body": "Most people assume plant fats are always better than animal fats. Coconut oil breaks that rule completely.",
                    "fats": [
                        {"name": "🥥 Coconut Oil", "type": "plant", "saturation": 90},
                        {"name": "🧈 Butter", "type": "animal", "saturation": 65},
                        {"name": "🫙 Ghee", "type": "animal", "saturation": 62},
                        {"name": "🥩 Lard", "type": "animal", "saturation": 40},
                        {"name": "🥜 Groundnut Oil", "type": "plant", "saturation": 17},
                        {"name": "🫒 Olive Oil", "type": "plant", "saturation": 14},
                        {"name": "🌻 Sunflower Oil", "type": "plant", "saturation": 10}
                    ],
                    "note": "🥥 Coconut oil's saturated fat is mainly lauric acid — which raises both HDL (good) and LDL. Unlike animal saturated fats, it may have a neutral or slightly positive net effect. Still — use in moderation at medium heat only."
                }
            },
            {
                "card_id": "fats_05",
                "number": "05",
                "label": "Myths Busted",
                "icon": "💥",
                "title": "6 Fat Lies the World Believed",
                "order": 5,
                "content": {
                    "type": "myths",
                    "body": "These myths shaped diets for decades — and made millions of people unhealthy.",
                    "myths": [
                        {"wrong": "Eating fat makes you fat", "right": "Excess calories cause fat gain — not dietary fat. Fat is satiating and actually prevents overeating"},
                        {"wrong": "Ghee is bad for your heart", "right": "Traditional ghee in moderation is fine — it contains butyrate, CLA & fat-soluble vitamins. The problem is excess"},
                        {"wrong": "Vegetable oils are heart-healthy", "right": "Refined seed oils (sunflower, soybean) are high in omega-6 and pro-inflammatory when overused"},
                        {"wrong": "Low-fat foods are healthier", "right": "Low-fat products replace fat with sugar & refined carbs — often worse for your metabolism"},
                        {"wrong": "Saturated fat causes heart disease", "right": "Multiple large meta-analyses found no clear link. Trans fats & refined carbs are the real culprits"},
                        {"wrong": "Eggs raise your cholesterol dangerously", "right": "Dietary cholesterol ≠ blood cholesterol. Your liver self-regulates — eggs are safe for most people"}
                    ]
                }
            },
            {
                "card_id": "fats_06",
                "number": "06",
                "label": "Omega-3 vs Omega-6 Crisis",
                "icon": "⚡",
                "title": "India's Silent Inflammation Epidemic",
                "order": 6,
                "content": {
                    "type": "omega_balance",
                    "body": "Both omega-3 and omega-6 are essential fats — your body cannot make them. But the balance matters enormously. Indians are dangerously out of balance.",
                    "ideal_ratio": "4:1",
                    "actual_ratio": "25:1",
                    "omega3_role": "Anti-inflammatory · Brain, heart, joints",
                    "omega6_role": "Pro-inflammatory in excess",
                    "info": [
                        {"icon": "🔴", "title": "Why So Much Omega-6?", "description": "Refined sunflower & soybean oils dominate Indian cooking — extremely high in omega-6"},
                        {"icon": "✅", "title": "Best Omega-3 Sources", "description": "Fatty fish (sardines, mackerel, rohu), flaxseeds, walnuts, chia seeds, mustard oil"},
                        {"icon": "⚠️", "title": "Chronic Imbalance = Chronic Inflammation", "description": "Sustained high omega-6:omega-3 ratio drives heart disease, arthritis, depression & cancer risk"}
                    ]
                }
            },
            {
                "card_id": "fats_07",
                "number": "07",
                "label": "The Real Villain",
                "icon": "☠️",
                "title": "Trans Fat — No Safe Level Exists",
                "order": 7,
                "content": {
                    "type": "process",
                    "body": "While saturated fat was being wrongly blamed, trans fat was quietly destroying hearts across India. It is the only fat with zero safe intake level.",
                    "steps": [
                        {"number": 1, "title": "How It's Made (Hydrogenation)", "description": "Liquid vegetable oil + hydrogen gas + metal catalyst + heat = solid trans fat. Cheap, shelf-stable, deadly"},
                        {"number": 2, "title": "Raises LDL (Bad Cholesterol)", "description": "Trans fat is the most potent raiser of LDL cholesterol — far more than saturated fat"},
                        {"number": 3, "title": "Lowers HDL (Good Cholesterol)", "description": "Simultaneously reduces protective HDL — a double blow to cardiovascular health"},
                        {"number": 4, "title": "Directly Inflames Arteries", "description": "Triggers arterial inflammation independently — the primary mechanism of heart attacks"}
                    ],
                    "hidden_sources": ["🫕 Vanaspati / Dalda", "🍪 Packaged Biscuits", "🍟 Street Fried Food", "🥐 Bakery Items", "🍿 Namkeen / Snacks", "🧁 Commercial Mithai"]
                }
            },
            {
                "card_id": "fats_08",
                "number": "08",
                "label": "Cholesterol Decoded",
                "icon": "🩺",
                "title": "Your Body Makes Its Own Cholesterol",
                "order": 8,
                "content": {
                    "type": "cholesterol",
                    "body": "Most people don't know this: your liver manufactures 70–80% of your blood cholesterol — regardless of what you eat.",
                    "liver_production": "75%",
                    "liver_note": "When you eat more cholesterol, your liver makes less. It's a self-regulating system — for most people.",
                    "types": [
                        {"name": "HDL — 'Good'", "description": "Carries cholesterol away from arteries back to liver for disposal. Higher = better. Target: >50 mg/dL"},
                        {"name": "LDL — 'Bad'", "description": "Deposits cholesterol in artery walls. But small dense LDL is dangerous — large fluffy LDL is harmless"}
                    ],
                    "egg_myth": "🥚 Egg myth busted: Eggs were demonised for their cholesterol. But dietary cholesterol has minimal impact on blood cholesterol for 75% of people. 2–3 eggs/day is safe for most healthy adults.",
                    "culprits": [
                        {"source": "☠️ Trans fats (vanaspati, dalda)", "impact": "Very High"},
                        {"source": "🍬 Refined carbs & sugar", "impact": "High"},
                        {"source": "🧬 Genetics (hyper-responders)", "impact": "Variable"},
                        {"source": "🧈 Excess saturated fat", "impact": "Moderate"},
                        {"source": "🥚 Dietary cholesterol (eggs)", "impact": "Minimal"}
                    ]
                }
            },
            {
                "card_id": "fats_09",
                "number": "09",
                "label": "Fat Per 100g",
                "icon": "📊",
                "title": "How Much Fat Is in Your Food?",
                "order": 9,
                "content": {
                    "type": "fat_bars",
                    "body": "Fat content per 100g — sorted by category, high to low.",
                    "categories": [
                        {
                            "name": "Animal Fats",
                            "emoji": "🥩",
                            "foods": [
                                {"emoji": "🫙", "name": "Ghee", "fat": 100, "note": "Pure fat — use sparingly, 1 tsp per meal max"},
                                {"emoji": "🧈", "name": "Butter", "fat": 81, "note": "High saturated fat — occasional use"},
                                {"emoji": "🧆", "name": "Paneer", "fat": 20, "note": "Good protein + fat combo — moderate portions"},
                                {"emoji": "🐟", "name": "Fatty Fish (Salmon/Mackerel)", "fat": 13, "note": "Best omega-3 source — eat 2–3x weekly"},
                                {"emoji": "🥚", "name": "Whole Egg", "fat": 10, "note": "Mostly in yolk — complete nutrition package"}
                            ]
                        },
                        {
                            "name": "Plant Fats",
                            "emoji": "🌿",
                            "foods": [
                                {"emoji": "🥥", "name": "Coconut Oil", "fat": 100, "note": "Pure fat, 90% saturated — medium heat only"},
                                {"emoji": "🥑", "name": "Avocado", "fat": 15, "note": "Mostly MUFA — heart-healthy, nutrient-dense"}
                            ]
                        },
                        {
                            "name": "Nuts & Seeds",
                            "emoji": "🌰",
                            "foods": [
                                {"emoji": "🪨", "name": "Walnuts", "fat": 65, "note": "Best plant omega-3 source (ALA)"},
                                {"emoji": "🌰", "name": "Almonds", "fat": 50, "note": "Mostly MUFA — handful daily is ideal"},
                                {"emoji": "🥜", "name": "Peanuts", "fat": 49, "note": "Mostly MUFA — affordable healthy fat"},
                                {"emoji": "🌱", "name": "Flaxseeds", "fat": 42, "note": "High omega-3 ALA — grind before eating"}
                            ]
                        }
                    ]
                }
            },
            {
                "card_id": "fats_10",
                "number": "10",
                "label": "Best Oils for Indian Cooking",
                "icon": "🍳",
                "title": "The Right Oil for the Right Heat",
                "order": 10,
                "content": {
                    "type": "cooking_oils",
                    "body": "Using the wrong oil at the wrong temperature creates harmful compounds. Smoke point matters.",
                    "groups": [
                        {
                            "level": "High Heat",
                            "emoji": "🔥",
                            "temp": ">200°C",
                            "usage": "Deep fry / Tadka",
                            "oils": ["🥜 Groundnut (South/West)", "🌿 Mustard (North/East/Bengal)"],
                            "note": "Both stable at high heat, traditional, regionally appropriate"
                        },
                        {
                            "level": "Medium Heat",
                            "emoji": "🌡️",
                            "temp": "150–200°C",
                            "usage": "Sauté / Curry",
                            "oils": ["🥥 Coconut (Kerala/Coastal)", "🌰 Sesame / Til (TN/Rajasthan)"],
                            "note": "Coconut ~175°C, sesame ~210°C — good for curries, not deep frying"
                        },
                        {
                            "level": "Cold / Finishing",
                            "emoji": "🥗",
                            "temp": "No cooking",
                            "usage": "No Heat",
                            "oils": ["🫒 Extra Virgin Olive Oil", "🌱 Flaxseed Oil"],
                            "note": "Use as dressings, drizzle on food after cooking. Flaxseed = best omega-3 plant source"
                        },
                        {
                            "level": "Avoid Completely",
                            "emoji": "❌",
                            "temp": "",
                            "usage": "",
                            "oils": ["🫕 Vanaspati / Dalda", "🌻 Excess Refined Sunflower", "🫘 Excess Soybean Oil"],
                            "note": "Trans fats + excessive omega-6 — primary drivers of inflammation & heart disease in India"
                        }
                    ]
                }
            },
            {
                "card_id": "fats_11",
                "number": "11",
                "label": "How Much Fat Per Day?",
                "icon": "⚖️",
                "title": "Fat Targets & Calorie Math",
                "order": 11,
                "content": {
                    "type": "fat_targets",
                    "body": "Fat is the most calorie-dense macronutrient at 9 kcal per gram.",
                    "example": "60kg person, 2000 kcal/day, 30% from fat: 2000 × 30% = 600 kcal ÷ 9 = ~67g fat/day",
                    "targets": [
                        {"who": "🪑 Sedentary Adult (2000 kcal)", "amount": "55–70g/day"},
                        {"who": "🏃 Active Adult (2500 kcal)", "amount": "70–95g/day"},
                        {"who": "📊 % of Total Calories", "amount": "20–35%"},
                        {"who": "🧈 Saturated Fat Max", "amount": "<10% calories"},
                        {"who": "☠️ Trans Fat", "amount": "Zero"}
                    ],
                    "common_foods": [
                        {"food": "1 tsp ghee", "fat": "5g"},
                        {"food": "1 tbsp oil", "fat": "14g"},
                        {"food": "30g almonds", "fat": "15g"},
                        {"food": "100g paneer", "fat": "20g"},
                        {"food": "1 whole egg", "fat": "5g"},
                        {"food": "30g walnuts", "fat": "20g"}
                    ]
                }
            },
            {
                "card_id": "fats_12",
                "number": "12",
                "label": "Smart Fat Day",
                "icon": "🗓️",
                "title": "Fat Meal Plan — 60kg Person (~65g fat)",
                "order": 12,
                "content": {
                    "type": "meal_plan",
                    "body": "Right fats at the right meals. Every meal has a fat source — but the right kind.",
                    "meals": [
                        {
                            "time": "Breakfast",
                            "icon": "🌅",
                            "total": "~18g fat",
                            "items": [
                                {"food": "🥚 2 whole eggs (scrambled in 1 tsp ghee)", "fat": 15},
                                {"food": "🌰 10 almonds (soaked overnight)", "fat": 5},
                                {"food": "🥛 1 glass whole milk", "fat": 5, "muted": True}
                            ]
                        },
                        {
                            "time": "Lunch",
                            "icon": "☀️",
                            "total": "~20g fat",
                            "items": [
                                {"food": "🐟 100g fish curry (mustard oil)", "fat": 15},
                                {"food": "🫘 Dal tadka (1 tsp groundnut oil)", "fat": 5},
                                {"food": "🍚 Small rice + sabzi", "fat": 2, "muted": True}
                            ]
                        },
                        {
                            "time": "Evening Snack",
                            "icon": "🌤️",
                            "total": "~12g fat",
                            "items": [
                                {"food": "🪨 4–5 walnuts", "fat": 13},
                                {"food": "🌱 1 tsp flaxseeds in curd", "fat": 2}
                            ]
                        },
                        {
                            "time": "Dinner",
                            "icon": "🌙",
                            "total": "~15g fat",
                            "items": [
                                {"food": "🧆 100g paneer sabzi (1 tsp oil)", "fat": 20},
                                {"food": "🫓 2 rotis + dal + salad", "fat": 3, "muted": True}
                            ]
                        }
                    ],
                    "daily_total": "~65g fat ✓"
                }
            },
            {
                "card_id": "fats_13",
                "number": "13",
                "label": "Summary",
                "icon": "✅",
                "title": "Your Fat Cheat Sheet",
                "order": 13,
                "content": {
                    "type": "summary",
                    "takeaways": [
                        "Fat was wrongly convicted — the low-fat era replaced fat with sugar and made us sicker",
                        "1g fat = 9 kcal — twice as calorie-dense as protein or carbs. Small amounts go a long way",
                        "Plant fat ≠ always good. Coconut oil is ~90% saturated — highest of any common fat or oil",
                        "Trans fat (vanaspati, dalda) is the only truly dangerous fat — no safe level exists",
                        "Your liver makes 70–80% of your blood cholesterol — dietary cholesterol has minimal impact for most",
                        "Indians eat 25x more omega-6 than omega-3 — chronic inflammation is the result",
                        "Ghee is okay sparingly — traditional wisdom had merit, but excess is still excess"
                    ],
                    "targets": [
                        {"who": "🪑 Sedentary (2000 kcal)", "amount": "55–70g fat/day"},
                        {"who": "🏃 Active (2500 kcal)", "amount": "70–95g fat/day"},
                        {"who": "📊 % of Calories", "amount": "20–35%"},
                        {"who": "🧈 Saturated Fat Max", "amount": "<10% calories"},
                        {"who": "☠️ Trans Fat", "amount": "Zero always"}
                    ],
                    "checklist": [
                        "Throw out vanaspati & dalda — replace with groundnut or mustard oil",
                        "Check packaged food labels for 'partially hydrogenated' — that means trans fat",
                        "Add omega-3 daily — walnuts, flaxseeds or fatty fish 2–3x a week",
                        "Stop fearing eggs — 2–3 whole eggs daily is safe for most healthy people",
                        "Use the right oil for the right heat — mustard/groundnut for high, coconut for medium",
                        "Limit ghee to 1 tsp per meal — enjoy it, don't eliminate it",
                        "Replace refined sunflower/soybean oil gradually with better alternatives"
                    ]
                }
            }
        ]
    }
]
