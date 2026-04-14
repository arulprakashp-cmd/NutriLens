"""Add 3 new topics: Fibre, Vitamins & Minerals, Hydration"""
import asyncio, os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')
client = AsyncIOMotorClient(os.environ['MONGO_URL'])
db = client[os.environ['DB_NAME']]

FIBRE_TOPIC = {
    "topic_id": "topic_fibre", "key": "fibre",
    "title": "The Fibre Story",
    "subtitle": "The nutrient most Indians ignore - most need",
    "icon_name": "leaf", "emoji": "🌿",
    "background_color": "#E8F0E4",
    "description": "11 cards - Gut health, weight loss, disease prevention & Indian sources",
    "card_count": 11, "order": 4,
    "cards": [
        {"card_id": "fibre_01", "number": "01", "label": "Reality Check", "icon": "📉",
         "title": "India Has a Severe Fibre Deficit", "order": 1,
         "content": {"type": "stats",
          "body": "As traditional diets gave way to ultra-processed foods, fibre quietly disappeared from Indian plates. The consequences are showing up everywhere - from constipation to cancer.",
          "stats": [
            {"value": "12g", "label": "Average daily fibre intake of most Indians - less than half the recommended amount"},
            {"value": "30g", "label": "Minimum recommended daily fibre intake for adults"},
            {"value": "70%", "label": "Indians who suffer from digestive problems - directly linked to low fibre intake"}
          ]}},
        {"card_id": "fibre_02", "number": "02", "label": "What Is Fibre?", "icon": "🌿",
         "title": "The Carb Your Body Can't Digest", "order": 2,
         "content": {"type": "split_comparison",
          "body": "Fibre is a type of carbohydrate found only in plant foods. Unlike other carbs, your body cannot break it down - and that's exactly what makes it so powerful.",
          "good": ["💧 Soluble Fibre", "Dissolves in water, forms gel", "Slows digestion & sugar absorption", "Sources: Oats, dal, apples, isabgol"],
          "bad": ["🪵 Insoluble Fibre", "Doesn't dissolve", "Adds bulk, speeds gut transit", "Sources: Whole wheat, bran, nuts"],
          "tip": "🌱 Only plant foods have fibre. Meat, fish, eggs and dairy contain zero fibre. Fibre provides almost zero calories yet is one of the most important things you can eat daily."}},
        {"card_id": "fibre_03", "number": "03", "label": "What Fibre Does", "icon": "⚙️",
         "title": "Six Ways Fibre Protects Your Body", "order": 3,
         "content": {"type": "benefits",
          "body": "Fibre is not just about digestion. It influences blood sugar, cholesterol, immunity, weight and even mood.",
          "benefits": [
            {"icon": "📉", "title": "Lowers Blood Sugar Spikes", "description": "Soluble fibre slows glucose absorption - eating rice with dal & sabzi cuts the GI of the whole meal"},
            {"icon": "❤️", "title": "Reduces LDL Cholesterol", "description": "Soluble fibre binds to cholesterol in the gut and removes it before it enters the bloodstream"},
            {"icon": "🦠", "title": "Feeds Gut Microbiome", "description": "Fibre ferments into short-chain fatty acids that nourish gut bacteria & reduce inflammation"},
            {"icon": "🙅", "title": "Controls Hunger", "description": "Expands in stomach, slows emptying, triggers fullness hormones - naturally prevents overeating"},
            {"icon": "🚿", "title": "Prevents Constipation", "description": "Insoluble fibre adds bulk and speeds gut transit time - keeping digestion regular and comfortable"},
            {"icon": "🛡️", "title": "Reduces Cancer Risk", "description": "High fibre intake is linked to 15-20% lower risk of colorectal cancer - one of India's rising cancers"}
          ]}},
        {"card_id": "fibre_04", "number": "04", "label": "Gut Microbiome", "icon": "🦠",
         "title": "You Have More Bacteria Than Cells", "order": 4,
         "content": {"type": "benefits",
          "body": "Your gut contains 38 trillion bacteria - more than the total number of human cells in your body. Fibre is what keeps them thriving.",
          "benefits": [
            {"icon": "🧠", "title": "Gut-Brain Axis", "description": "90% of serotonin (your mood chemical) is made in the gut. Healthy microbiome = better mood & lower anxiety"},
            {"icon": "🛡️", "title": "Immunity Headquarters", "description": "70% of the immune system lives in the gut. Diverse gut bacteria = stronger immune response"},
            {"icon": "⚗️", "title": "Short-Chain Fatty Acids", "description": "Bacteria ferment fibre into butyrate, propionate & acetate - which reduce inflammation & protect the gut lining"},
            {"icon": "⚖️", "title": "Metabolism Control", "description": "Gut bacteria influence how many calories you extract from food and how fat is stored"}
          ],
          "callout": "💡 Diversity is key. Eating 30+ different plant foods per week dramatically improves gut bacteria diversity."}},
        {"card_id": "fibre_05", "number": "05", "label": "Fibre & Weight Loss", "icon": "⚖️",
         "title": "The Natural Appetite Suppressant", "order": 5,
         "content": {"type": "process",
          "body": "Fibre doesn't burn fat directly - but it creates the conditions where eating less feels effortless.",
          "steps": [
            {"number": 1, "title": "Expands in the Stomach", "description": "Soluble fibre absorbs water and swells - physically filling the stomach and triggering stretch receptors"},
            {"number": 2, "title": "Slows Stomach Emptying", "description": "Food stays in the stomach longer, keeping you full for 3-4 hours instead of 1-2 hours"},
            {"number": 3, "title": "Triggers Fullness Hormones", "description": "Fibre stimulates GLP-1 and PYY - the same hormones targeted by popular weight-loss drugs"},
            {"number": 4, "title": "Reduces Calorie Absorption", "description": "Fibre slightly reduces the calories absorbed from fat and protein eaten in the same meal"},
            {"number": 5, "title": "Kills Sugar Cravings", "description": "Stable blood sugar from fibre means no energy crashes and no desperate need for sweets after meals"}
          ],
          "callout": "🔬 Studies show people who increase fibre by just 14g/day spontaneously eat 10% fewer calories - without dieting."}},
        {"card_id": "fibre_06", "number": "06", "label": "Disease Prevention", "icon": "🛡️",
         "title": "The Most Protective Nutrient You're Ignoring", "order": 6,
         "content": {"type": "benefits",
          "body": "Decades of research consistently show that high fibre intake dramatically reduces the risk of India's most common chronic diseases.",
          "benefits": [
            {"icon": "🩸", "title": "Type 2 Diabetes - 20-30% lower risk", "description": "Slows glucose absorption, reduces insulin spikes, improves insulin sensitivity over time"},
            {"icon": "❤️", "title": "Heart Disease - 15-25% lower risk", "description": "Lowers LDL cholesterol, reduces blood pressure, decreases arterial inflammation"},
            {"icon": "🎗️", "title": "Colorectal Cancer - 15-20% lower risk", "description": "Speeds waste through colon, dilutes carcinogens, feeds protective bacteria that produce butyrate"},
            {"icon": "⚖️", "title": "Obesity - consistent weight loss link", "description": "Higher satiety, lower calorie density, reduced fat absorption - naturally keeps weight in check"}
          ],
          "callout": "📚 A 2019 Lancet meta-analysis of 185 studies found people eating the most fibre had 15-30% lower mortality from all causes."}},
        {"card_id": "fibre_07", "number": "07", "label": "Fibre Per 100g", "icon": "📊",
         "title": "How Much Fibre Is in Your Food?", "order": 7,
         "content": {"type": "protein_bars",
          "body": "Sorted by category, high to low. All values per 100g.",
          "categories": [
            {"name": "Legumes & Pulses", "emoji": "🫘", "foods": [
              {"emoji": "🫘", "name": "Rajma (Kidney Beans)", "protein": 15, "note": "Best fibre source in Indian diet"},
              {"emoji": "🫛", "name": "Chickpeas / Chana", "protein": 12, "note": "Soluble + insoluble - excellent combo"},
              {"emoji": "🟤", "name": "Masoor / Toor Dal (dry)", "protein": 11, "note": "Everyday dal = everyday fibre"}
            ]},
            {"name": "Grains & Cereals", "emoji": "🌾", "foods": [
              {"emoji": "🌾", "name": "Oats (rolled, dry)", "protein": 10, "note": "High beta-glucan - best for cholesterol"},
              {"emoji": "🌾", "name": "Whole Wheat / Atta", "protein": 7, "note": "Far better than maida - keep the bran!"},
              {"emoji": "🌾", "name": "Brown Rice (cooked)", "protein": 2, "note": "Still better than white rice (0.4g)"}
            ]},
            {"name": "Nuts & Seeds", "emoji": "🌰", "foods": [
              {"emoji": "🌱", "name": "Flaxseeds / Alsi", "protein": 27, "note": "Highest fibre density of any common food!"},
              {"emoji": "🌰", "name": "Almonds", "protein": 12, "note": "Protein + fat + fibre - ideal snack"}
            ]}
          ]}},
        {"card_id": "fibre_08", "number": "08", "label": "Soluble vs Insoluble", "icon": "🔬",
         "title": "Which Type Does What?", "order": 8,
         "content": {"type": "split_comparison",
          "body": "Both types are essential - but they work very differently in your body. You need both every day.",
          "good": ["💧 Soluble Fibre", "✅ Lowers blood sugar", "✅ Lowers LDL cholesterol", "✅ Feeds gut bacteria", "✅ Reduces hunger", "Best: Oats, dal, apple, carrots"],
          "bad": ["🪵 Insoluble Fibre", "✅ Prevents constipation", "✅ Reduces colon cancer", "✅ Cleanses gut wall", "✅ Adds stool bulk", "Best: Wheat bran, nuts, leafy greens"],
          "tip": "💡 Most whole plant foods contain both types. Eating a variety of legumes, whole grains, vegetables & fruits naturally gives you the right balance.\n\n⚠️ Increase fibre gradually - adding too much too fast causes bloating & gas. Go up by 5g/week and drink plenty of water."}},
        {"card_id": "fibre_09", "number": "09", "label": "Daily Fibre Plan", "icon": "🗓️",
         "title": "How to Hit 30g Fibre in a Day", "order": 9,
         "content": {"type": "meal_plan",
          "body": "Real Indian meals that make 30g fibre feel effortless - no supplements needed.",
          "meals": [
            {"time": "Breakfast", "icon": "🌅", "total": "~9g fibre", "items": [
              {"food": "🌾 1 bowl oats with banana", "protein": 10},
              {"food": "🌱 1 tsp flaxseeds (ground)", "protein": 2},
              {"food": "🥛 Milk / curd", "protein": 0, "muted": True}
            ]},
            {"time": "Lunch", "icon": "☀️", "total": "~11g fibre", "items": [
              {"food": "🫘 1 katori rajma / chana curry", "protein": 8},
              {"food": "🌾 1 cup brown rice", "protein": 2},
              {"food": "🥗 Mixed sabzi (bhindi/methi)", "protein": 3}
            ]},
            {"time": "Evening Snack", "icon": "🌤️", "total": "~5g fibre", "items": [
              {"food": "🍎 1 apple with skin", "protein": 4},
              {"food": "🌰 10 almonds", "protein": 3}
            ]},
            {"time": "Dinner", "icon": "🌙", "total": "~9g fibre", "items": [
              {"food": "🟤 2 katori dal (masoor/toor)", "protein": 8},
              {"food": "🫓 2 whole wheat rotis", "protein": 4},
              {"food": "🥦 Seasonal sabzi + salad", "protein": 3}
            ]}
          ],
          "daily_total": "~34g fibre ✓"}},
        {"card_id": "fibre_10", "number": "10", "label": "Summary", "icon": "✅",
         "title": "Your Fibre Cheat Sheet", "order": 10,
         "content": {"type": "summary",
          "takeaways": [
            "Most Indians eat only 12g fibre/day - less than half the recommended 30g minimum",
            "Fibre is a carb your body can't digest - but your gut bacteria can. They convert it to health-protective compounds",
            "Soluble fibre (oats, dal) lowers blood sugar & cholesterol. Insoluble fibre (whole grains, vegetables) prevents constipation & cancer",
            "38 trillion gut bacteria depend on fibre - a diverse, fibre-rich diet improves immunity, mood & metabolism",
            "High fibre reduces risk of diabetes by 20-30%, heart disease by 15-25%, and colorectal cancer by 15-20%",
            "Flaxseeds (27g/100g) and rajma (15g/100g) are India's most powerful fibre sources - use them daily"
          ],
          "targets": [
            {"who": "👨 Adult Men", "amount": "38g / day"},
            {"who": "👩 Adult Women", "amount": "25g / day"},
            {"who": "🧒 Children (9-13)", "amount": "26-31g / day"},
            {"who": "🌿 Minimum for all", "amount": "30g / day"},
            {"who": "💧 Water needed with fibre", "amount": "8-10 glasses"}
          ]}},
        {"card_id": "fibre_checklist", "number": "11", "label": "Action Checklist", "icon": "📋",
         "title": "Your Action Plan", "order": 11,
         "content": {"type": "checklist",
          "body": "Start with these simple steps today. Small changes lead to big results.",
          "checklist": [
            "Add 1 tbsp ground flaxseeds to breakfast daily - easiest 3g fibre upgrade",
            "Eat dal at least once a day - toor, masoor or chana all count",
            "Switch from white rice to brown rice or reduce rice + add more sabzi",
            "Eat fruit with skin (apple, guava, pear) - the skin has most of the fibre",
            "Replace biscuit snacks with a handful of almonds or roasted chana",
            "Increase fibre gradually (5g/week) and drink more water to avoid bloating",
            "Aim for 30+ different plant foods per week for maximum gut bacteria diversity"
          ]}}
    ]
}

VITAMINS_TOPIC = {
    "topic_id": "topic_vitamins", "key": "vitamins",
    "title": "The Vitamins & Minerals Story",
    "subtitle": "The micronutrients that run everything",
    "icon_name": "medkit", "emoji": "💊",
    "background_color": "#E4ECF4",
    "description": "13 cards - D, B12, Iron, Calcium, Zinc deficiencies & supplements guide",
    "card_count": 13, "order": 5,
    "cards": [
        {"card_id": "vit_01", "number": "01", "label": "Reality Check", "icon": "🚨",
         "title": "India's Hidden Micronutrient Crisis", "order": 1,
         "content": {"type": "stats",
          "body": "India has abundant food yet faces widespread micronutrient deficiencies. We eat enough calories - but not enough vitamins and minerals. This is called 'hidden hunger.'",
          "stats": [
            {"value": "76%", "label": "Indians Vitamin D deficient - despite abundant sunshine"},
            {"value": "50%", "label": "Indian women anaemic (Iron) - worst in the world"},
            {"value": "47%", "label": "Vegetarians Vitamin B12 deficient - nervous system at risk"},
            {"value": "40%", "label": "Indians Calcium deficient - bone loss epidemic brewing"}
          ]}},
        {"card_id": "vit_02", "number": "02", "label": "Types of Vitamins", "icon": "🔬",
         "title": "Fat-Soluble vs Water-Soluble", "order": 2,
         "content": {"type": "split_comparison",
          "body": "The most important distinction in vitamins - it determines how they're absorbed, stored and whether you can overdose.",
          "good": ["🧈 Fat-Soluble", "Stored in fat tissue & liver", "Can build up - excess is toxic", "A · D · E · K", "Need fat to absorb"],
          "bad": ["💧 Water-Soluble", "Not stored - flushed daily", "Must eat them every day", "B1·B2·B3·B5·B6·B7·B9·B12·C", "Cooking destroys many"],
          "tip": "💡 Low-fat diet = vitamin deficiency. Vitamins A, D, E & K cannot be absorbed without dietary fat. Never eat salads or vegetables without some oil."}},
        {"card_id": "vit_03", "number": "03", "label": "Vitamin D", "icon": "☀️",
         "title": "India's Sunshine Paradox", "order": 3,
         "content": {"type": "benefits",
          "body": "India gets more sunshine than almost anywhere - yet 76% of Indians are Vitamin D deficient. How is this possible?",
          "benefits": [
            {"icon": "🌑", "title": "Darker Skin Needs More Sun", "description": "Melanin reduces Vitamin D synthesis. Dark-skinned Indians need 3-5x more sun exposure than fair-skinned Europeans"},
            {"icon": "👗", "title": "Clothing Covers Skin", "description": "Vitamin D is made in exposed skin only. Full-coverage clothing blocks synthesis almost completely"},
            {"icon": "🏢", "title": "Indoor Lifestyle", "description": "Office workers, students & urban Indians spend 90% of their day indoors - glass blocks UV-B rays"},
            {"icon": "🕛", "title": "Wrong Time of Day", "description": "Only 10am-2pm sun produces Vitamin D. Morning walks and evening walks produce almost none"}
          ],
          "callout": "✅ Fix: 15-20 min midday sun on arms & legs daily. Most Indians need Vitamin D3 supplement (1000-2000 IU/day) - test first."}},
        {"card_id": "vit_04", "number": "04", "label": "Vitamin B12", "icon": "🧬",
         "title": "The Vegetarian Blind Spot", "order": 4,
         "content": {"type": "benefits",
          "body": "Vitamin B12 exists only in animal foods. There is no reliable plant source. 47% of Indian vegetarians are deficient - with consequences that can become permanent.",
          "benefits": [
            {"icon": "🧠", "title": "Brain & Nervous System", "description": "B12 maintains the myelin sheath around nerves. Deficiency causes numbness, memory loss & cognitive decline"},
            {"icon": "🩸", "title": "Red Blood Cell Formation", "description": "Without B12, red blood cells become abnormally large and can't carry oxygen efficiently - fatigue & weakness"},
            {"icon": "💔", "title": "Heart Risk", "description": "B12 deficiency raises homocysteine levels - a direct risk factor for heart disease and stroke"},
            {"icon": "😔", "title": "Depression & Mood", "description": "B12 is needed to produce serotonin and dopamine. Deficiency is strongly linked to depression"}
          ],
          "callout": "💊 Vegetarians must supplement: B12 500mcg daily or 1000mcg every other day. Methylcobalamin form is best absorbed."}},
        {"card_id": "vit_05", "number": "05", "label": "Iron", "icon": "🩸",
         "title": "India's Anaemia Epidemic", "order": 5,
         "content": {"type": "split_comparison",
          "body": "India has the highest anaemia burden in the world. 50% of Indian women and 60% of children under 5 are anaemic - iron deficiency is the primary cause.",
          "good": ["🥩 Heme Iron", "25-30% absorbed", "From animal foods", "Highly bioavailable", "Body absorbs it easily"],
          "bad": ["🌿 Non-Heme Iron", "2-8% absorbed", "From plant foods", "Much harder to absorb", "Improved by Vitamin C"],
          "tip": "💡 The Vitamin C hack: Adding lemon juice to dal, eating tomatoes with spinach, or having an orange after an iron-rich meal can increase iron absorption by 2-3x.\n\n☕ Avoid tea/coffee with meals - tannins block iron absorption by up to 60%."}},
        {"card_id": "vit_06", "number": "06", "label": "Calcium", "icon": "🦴",
         "title": "Not Just About Milk", "order": 6,
         "content": {"type": "benefits",
          "body": "Calcium is the most abundant mineral in the body - 99% in bones and teeth. Many Indians avoid dairy and don't know the alternatives. Most Indians get 400-500mg - less than half the 1000mg daily requirement.",
          "benefits": [
            {"icon": "🌾", "title": "Ragi (Finger Millet)", "description": "364mg calcium per 100g - more than milk. Ragi roti or porridge daily is India's best kept calcium secret"},
            {"icon": "🌱", "title": "Sesame Seeds (Til) - 975mg/100g", "description": "Highest calcium density of any food. Add til to rotis, chutneys and laddoos daily"},
            {"icon": "🥬", "title": "Amaranth & Green Leafy", "description": "Rajgira, methi, moringa leaves - all excellent calcium sources used in traditional Indian cooking"},
            {"icon": "🥛", "title": "Dairy - 300mg per glass milk", "description": "Milk, curd, paneer - highly bioavailable calcium. 2-3 servings daily covers most needs"}
          ],
          "callout": "⚠️ Calcium needs Vitamin D to absorb. Without adequate Vitamin D, even high calcium intake does little for bone health."}},
        {"card_id": "vit_07", "number": "07", "label": "Zinc", "icon": "🛡️",
         "title": "The Most Underrated Mineral", "order": 7,
         "content": {"type": "benefits",
          "body": "Zinc is involved in over 300 enzyme reactions in the body. Yet it gets almost no attention - and 30% of Indians are deficient, especially vegetarians.",
          "benefits": [
            {"icon": "🦠", "title": "Immune Defence", "description": "Zinc activates T-cells that fight infection. Deficiency means more frequent colds, infections & slower recovery"},
            {"icon": "🩹", "title": "Wound Healing", "description": "Essential for cell repair and skin regeneration. Slow-healing wounds are a classic sign of zinc deficiency"},
            {"icon": "👅", "title": "Taste & Smell", "description": "Loss of taste and smell - even without illness - is a hallmark symptom of zinc deficiency"},
            {"icon": "🧒", "title": "Child Growth", "description": "Zinc deficiency is a leading cause of stunted growth in Indian children - severely under-recognised"},
            {"icon": "💊", "title": "Hormone Production", "description": "Required for testosterone, insulin and thyroid hormone production. Deficiency affects fertility in both sexes"}
          ],
          "callout": "Best sources: Eggs, Chicken, Rajma, Pumpkin Seeds, Cashews, Whole Wheat, Paneer. Plant zinc is poorly absorbed - vegetarians need 50% more."}},
        {"card_id": "vit_08", "number": "08", "label": "Vitamin Quick Ref", "icon": "📋",
         "title": "All Key Vitamins at a Glance", "order": 8,
         "content": {"type": "benefits",
          "body": "Quick reference for the most important vitamins and their best Indian food sources.",
          "benefits": [
            {"icon": "🅰️", "title": "Vitamin A - Vision, immunity, skin", "description": "Carrots, sweet potato, liver, eggs"},
            {"icon": "☀️", "title": "Vitamin D - Calcium absorption, mood", "description": "Sunlight, fatty fish, egg yolk, fortified milk"},
            {"icon": "🅴", "title": "Vitamin E - Antioxidant, skin health", "description": "Almonds, sunflower seeds, olive oil"},
            {"icon": "🅺", "title": "Vitamin K - Blood clotting, bones", "description": "Spinach, methi, broccoli, green leafy veg"},
            {"icon": "🍋", "title": "Vitamin C - Immunity, iron booster", "description": "Amla, guava, lemon, tomato, capsicum"},
            {"icon": "🧬", "title": "Vitamin B12 - Nerves, red blood cells", "description": "Eggs, fish, milk - NO plant sources"},
            {"icon": "🥬", "title": "Folate (B9) - Pregnancy, cell division", "description": "Dal, methi, spinach, chickpeas"}
          ]}},
        {"card_id": "vit_09", "number": "09", "label": "Mineral Quick Ref", "icon": "⚗️",
         "title": "Key Minerals Every Indian Needs", "order": 9,
         "content": {"type": "benefits",
          "body": "Essential minerals, their functions, deficiency signs and best Indian food sources.",
          "benefits": [
            {"icon": "⚡", "title": "Iron - Oxygen transport, energy", "description": "Dal, rajma, spinach, meat, eggs + Vitamin C. Women need 18mg/day"},
            {"icon": "🦴", "title": "Calcium - Bones, muscles, nerves", "description": "Milk, ragi, sesame, rajgira, green leafy. Need 1000mg/day"},
            {"icon": "🛡️", "title": "Zinc - Immunity, healing, growth", "description": "Eggs, meat, rajma, pumpkin seeds, cashews. Men 11mg, Women 8mg"},
            {"icon": "💪", "title": "Magnesium - 300+ enzyme reactions", "description": "Nuts, seeds, dark chocolate, leafy greens, dal. Need 320-420mg/day"},
            {"icon": "🫀", "title": "Potassium - Heart rhythm, BP", "description": "Banana, potato, coconut water, dal, avocado. Need 3500mg/day"},
            {"icon": "🦋", "title": "Iodine - Thyroid, metabolism", "description": "Iodised salt, seafood, dairy, eggs. Need 150mcg/day"}
          ]}},
        {"card_id": "vit_10", "number": "10", "label": "Supplement Guide", "icon": "💊",
         "title": "Which Supplements Do Indians Actually Need?", "order": 10,
         "content": {"type": "fat_types",
          "body": "Not all supplements are necessary - some are essential, some are situational, some are a waste of money.",
          "types": [
            {"level": "good1", "icon": "☀️", "name": "Vitamin D3 - Most Indians Need", "description": "76% of Indians are deficient. 1000-2000 IU/day is safe for most. Test 25-OH-D levels first.", "examples": "Target: 40-60 ng/mL"},
            {"level": "good2", "icon": "🧬", "name": "Vitamin B12 - Vegetarians Must Take", "description": "No reliable plant source exists. 500mcg daily or 1000mcg alternate days. Methylcobalamin form is best.", "examples": "Essential for all vegetarians"},
            {"level": "warn", "icon": "🩸", "name": "Iron - Women & Anaemic Persons", "description": "Test ferritin levels first. Do not supplement without deficiency - excess iron causes oxidative damage.", "examples": "Take with Vitamin C for absorption"},
            {"level": "bad", "icon": "🧴", "name": "Multivitamins - Usually Unnecessary", "description": "Most multivitamins have poor bioavailability and wrong doses. Better to address specific deficiencies.", "examples": "Targeted supplements > multivitamins"}
          ]}},
        {"card_id": "vit_11", "number": "11", "label": "Micronutrient-Rich Day", "icon": "🗓️",
         "title": "A Day That Covers Key Deficiencies", "order": 11,
         "content": {"type": "meal_plan",
          "body": "Targeting Vitamin D, B12, Iron, Calcium & Zinc in real Indian meals.",
          "meals": [
            {"time": "Breakfast", "icon": "🌅", "total": "B12 · D · Calcium", "items": [
              {"food": "🥚 2 whole eggs (omelette)", "protein": 0},
              {"food": "🥛 1 glass fortified milk", "protein": 0},
              {"food": "🌾 Ragi roti or oats", "protein": 0}
            ]},
            {"time": "Lunch", "icon": "☀️", "total": "Iron · Zinc · Folate", "items": [
              {"food": "🫘 Rajma / chana curry", "protein": 0},
              {"food": "🥬 Palak sabzi + lemon squeeze", "protein": 0},
              {"food": "🌾 Brown rice + whole wheat roti", "protein": 0}
            ]},
            {"time": "Snack", "icon": "🌤️", "total": "Zinc · Vitamin E · Ca", "items": [
              {"food": "🌰 10 almonds + 5 cashews", "protein": 0},
              {"food": "🌱 1 tsp sesame seeds in curd", "protein": 0}
            ]},
            {"time": "Dinner", "icon": "🌙", "total": "B12 · Iron · Potassium", "items": [
              {"food": "🐟 Fish curry / 100g paneer", "protein": 0},
              {"food": "🟤 Dal tadka (masoor/toor)", "protein": 0},
              {"food": "🍌 Banana before bed", "protein": 0}
            ]}
          ]}},
        {"card_id": "vit_12", "number": "12", "label": "Summary", "icon": "✅",
         "title": "Your Vitamins & Minerals Cheat Sheet", "order": 12,
         "content": {"type": "summary",
          "takeaways": [
            "India faces a silent micronutrient crisis - D, B12, Iron, Calcium and Zinc deficiencies are widespread",
            "Fat-soluble vitamins (A,D,E,K) need fat to absorb and can accumulate - never eat vegetables without oil",
            "Vitamin B12 exists only in animal foods - vegetarians must supplement without exception",
            "76% of Indians are Vitamin D deficient despite abundant sunshine - skin tone, clothing and timing are the reasons",
            "Lemon juice on iron-rich food increases absorption by 2-3x. Tea and coffee block it by 60%",
            "Ragi and sesame seeds are India's most underrated calcium sources - better than milk by weight",
            "Test D, B12 and iron (ferritin) levels annually - supplement only what you're deficient in"
          ],
          "targets": [
            {"who": "🌿 All Vegetarians", "amount": "B12 supplement"},
            {"who": "☀️ All Indians", "amount": "Vitamin D test + likely D3"},
            {"who": "👩 Women (15-49)", "amount": "Iron test + folate"},
            {"who": "🤰 Pregnant Women", "amount": "D3 + B12 + Iron + Folate"},
            {"who": "🧒 Children", "amount": "D3 + Iron + Zinc"}
          ]}},
        {"card_id": "vit_checklist", "number": "13", "label": "Action Checklist", "icon": "📋",
         "title": "Your Action Plan", "order": 13,
         "content": {"type": "checklist",
          "body": "Start with these simple steps today.",
          "checklist": [
            "Get blood test for Vitamin D, B12, ferritin (iron) and calcium once a year",
            "If vegetarian, start B12 supplement (methylcobalamin 500mcg daily) now",
            "Squeeze lemon on dal and spinach at every meal - it doubles iron absorption",
            "Add ragi roti or til (sesame) to weekly meals for calcium beyond dairy",
            "Spend 15 minutes in midday sun (10am-2pm) with arms exposed, at least 4x/week",
            "Stop drinking tea or coffee within 1 hour of iron-rich meals",
            "Never eat salads or vegetables without a little oil - fat-soluble vitamins need it"
          ]}}
    ]
}

HYDRATION_TOPIC = {
    "topic_id": "topic_hydration", "key": "hydration",
    "title": "The Hydration Story",
    "subtitle": "Water - the forgotten nutrient - India's chronic shortfall",
    "icon_name": "water", "emoji": "💧",
    "background_color": "#E0F0F4",
    "description": "11 cards - How much water, electrolytes, traditional drinks & daily plan",
    "card_count": 11, "order": 6,
    "cards": [
        {"card_id": "hyd_01", "number": "01", "label": "Reality Check", "icon": "💧",
         "title": "Most Indians Are Chronically Dehydrated", "order": 1,
         "content": {"type": "stats",
          "body": "Dehydration isn't just about feeling thirsty. By the time thirst kicks in, you're already 1-2% dehydrated - enough to impair performance and cognition.",
          "stats": [
            {"value": "60%", "label": "of your body is water"},
            {"value": "75%", "label": "of your brain is water"},
            {"value": "83%", "label": "of your blood is water"}
          ]}},
        {"card_id": "hyd_02", "number": "02", "label": "Why Water Is Life", "icon": "🌊",
         "title": "Every Reaction in Your Body Needs Water", "order": 2,
         "content": {"type": "benefits",
          "body": "Water is not just a drink - it is the medium in which life happens. Without enough water, every system slows down.",
          "benefits": [
            {"icon": "🩸", "title": "Nutrient Transport", "description": "Blood (83% water) carries oxygen, glucose, vitamins and minerals to every cell"},
            {"icon": "🌡️", "title": "Temperature Regulation", "description": "Sweating and breathing release water to cool the body - essential in India's heat"},
            {"icon": "🧹", "title": "Waste Removal", "description": "Kidneys use water to filter 180 litres of blood daily and flush toxins out through urine"},
            {"icon": "🦴", "title": "Joint Lubrication", "description": "Synovial fluid (mostly water) cushions joints. Dehydration causes joint pain and cartilage wear"},
            {"icon": "🍽️", "title": "Digestion & Absorption", "description": "Saliva, stomach acid, digestive enzymes and intestinal fluids are all mostly water"},
            {"icon": "✨", "title": "Skin Health", "description": "Well-hydrated skin is plumper, more elastic and less prone to wrinkles"}
          ]}},
        {"card_id": "hyd_03", "number": "03", "label": "How Much Water", "icon": "🧮",
         "title": "The '8 Glasses' Rule Is Wrong", "order": 3,
         "content": {"type": "process",
          "body": "The popular '8 glasses a day' advice has no scientific basis. Actual water needs depend on your weight, activity and climate.",
          "steps": [
            {"number": 1, "title": "Base: Body weight (kg) x 35ml", "description": "This is your starting point. A 60kg person needs at least 2100ml"},
            {"number": 2, "title": "+500ml per hour of exercise", "description": "Physical activity and sweating increase needs significantly"},
            {"number": 3, "title": "+500-1000ml in hot weather", "description": "Indian summers can cause 1-2 litres of water loss per hour through sweat"},
            {"number": 4, "title": "+1-2L during illness", "description": "Fever, vomiting or diarrhoea dramatically increase water needs"},
            {"number": 5, "title": "Food provides ~20% of water", "description": "Fruits, vegetables and cooked foods contribute about 500ml daily"}
          ],
          "callout": "Example: 60kg person, moderate activity in summer: 60x35 = 2100ml + 500ml heat = ~2.6 litres/day"}},
        {"card_id": "hyd_04", "number": "04", "label": "Signs of Dehydration", "icon": "🚨",
         "title": "Your Body's Dehydration Warning System", "order": 4,
         "content": {"type": "fat_types",
          "body": "Urine colour is the most reliable daily indicator of hydration. Check the toilet, not the clock.",
          "types": [
            {"level": "good1", "icon": "🟡", "name": "Mild Dehydration - 1-2% body weight loss", "description": "Thirst, dry mouth, headache, reduced concentration, darker urine, fatigue", "examples": "~500ml-1L water deficit"},
            {"level": "warn", "icon": "🟠", "name": "Moderate Dehydration - 3-5% loss", "description": "Dizziness, rapid heartbeat, muscle cramps, very little urine, irritability", "examples": "~1.5-2.5L water deficit"},
            {"level": "bad", "icon": "🔴", "name": "Severe Dehydration - >6% loss", "description": "Confusion, sunken eyes, no urine output, rapid breathing - medical emergency", "examples": ">3L water deficit - seek medical help"}
          ]}},
        {"card_id": "hyd_05", "number": "05", "label": "Water vs Other Drinks", "icon": "🥤",
         "title": "What Actually Hydrates You?", "order": 5,
         "content": {"type": "benefits",
          "body": "Not all liquids hydrate equally. Some actively hydrate, some partially, and some actually dehydrate you further.",
          "benefits": [
            {"icon": "💧", "title": "Water - Best hydration", "description": "Zero calories, kidney-protective. Add a pinch of salt in heat for electrolytes"},
            {"icon": "🥥", "title": "Coconut Water - Excellent", "description": "Natural electrolytes (potassium, sodium), low sugar, excellent for rehydration after sweat"},
            {"icon": "🥛", "title": "Buttermilk / Chaas - Excellent", "description": "Probiotics + electrolytes + hydration. Traditional Indian wisdom - ideal summer drink"},
            {"icon": "☕", "title": "Tea / Coffee - Moderate", "description": "Mild diuretic - net effect is slightly positive at 1-2 cups. Problem is 4-6 cups"},
            {"icon": "🥤", "title": "Soft Drinks / Sodas - Avoid", "description": "High sugar triggers insulin spike, promotes dehydration, zero nutrition"}
          ]}},
        {"card_id": "hyd_06", "number": "06", "label": "Hydration & Weight", "icon": "⚖️",
         "title": "Water Is Your Free Weight Loss Tool", "order": 6,
         "content": {"type": "benefits",
          "body": "Most people overlook water when trying to lose weight. But strategic hydration significantly reduces calorie intake.",
          "benefits": [
            {"icon": "🥛", "title": "500ml Before Each Meal", "description": "Reduces meal calorie intake by 13% on average. Fills the stomach, slows eating"},
            {"icon": "🧠", "title": "Thirst Mistaken for Hunger", "description": "The hypothalamus controls both signals - they're easy to confuse. Try water before food"},
            {"icon": "🔥", "title": "Cold Water Boosts Metabolism", "description": "Body burns ~8 extra calories warming cold water to body temperature. Adds up over a day"},
            {"icon": "💪", "title": "Better Exercise Performance", "description": "Even mild dehydration cuts strength & endurance by 10-20%"},
            {"icon": "🚿", "title": "Flushes Retained Bloat", "description": "Counterintuitively, drinking more water reduces water retention"}
          ],
          "callout": "💡 Try this before every snack: Drink a full glass of water and wait 15 minutes. This simple trick alone can cut 200-300 calories daily."}},
        {"card_id": "hyd_07", "number": "07", "label": "Electrolytes", "icon": "⚡",
         "title": "Not Just Water - Minerals Matter Too", "order": 7,
         "content": {"type": "benefits",
          "body": "When you sweat heavily, you lose not just water but electrolytes - minerals that conduct electrical signals. Plain water alone can't always replace them.",
          "benefits": [
            {"icon": "⚡", "title": "Sodium", "description": "Fluid balance, nerve signals, blood pressure. Sources: Salt, chaas, coconut water, ORS"},
            {"icon": "🍌", "title": "Potassium", "description": "Heart rhythm, muscle function, counters sodium. Sources: Banana, coconut water, potato, dal"},
            {"icon": "💪", "title": "Magnesium", "description": "Muscle relaxation, nerve function, energy. Sources: Nuts, seeds, leafy greens, dark chocolate"},
            {"icon": "🦴", "title": "Calcium", "description": "Muscle contractions, nerve signals. Sources: Milk, curd, ragi, sesame seeds"}
          ],
          "callout": "🧂 Use ORS for: intense outdoor work, >1hr exercise, fever/illness, diarrhoea/vomiting. Plain water is fine for normal daily activity."}},
        {"card_id": "hyd_08", "number": "08", "label": "Traditional Indian Hydration", "icon": "🏺",
         "title": "Ancient Wisdom Was Right", "order": 8,
         "content": {"type": "benefits",
          "body": "Long before sports drinks, Indian tradition had perfect hydration solutions for a hot, humid climate. Most are still the best options today.",
          "benefits": [
            {"icon": "🥥", "title": "Nariyal Pani (Coconut Water)", "description": "Nature's isotonic drink - same electrolyte concentration as blood. Perfect post-sweat rehydration"},
            {"icon": "🥛", "title": "Chaas / Buttermilk", "description": "Probiotics + calcium + sodium + water. Cools the gut, aids digestion, prevents dehydration in heat"},
            {"icon": "🍋", "title": "Nimbu Pani (Lemon Water)", "description": "Water + Vitamin C + sodium (salt) + natural sugar. Simple, effective, affordable hydration"},
            {"icon": "🌿", "title": "Aam Panna (Raw Mango Drink)", "description": "Prevents heat stroke, rich in electrolytes & Vitamin C. Made with raw mango, cumin, salt & mint"},
            {"icon": "🌾", "title": "Kanji (Fermented Rice/Carrot Water)", "description": "Fermented drink with probiotics, natural electrolytes. Traditional North/East Indian summer cooler"}
          ],
          "callout": "🏺 These drinks predate packaged beverages by centuries - designed for India's climate, using locally available ingredients. Far superior to commercial sports drinks."}},
        {"card_id": "hyd_09", "number": "09", "label": "Daily Hydration Plan", "icon": "🗓️",
         "title": "When to Drink - Timing Matters", "order": 9,
         "content": {"type": "meal_plan",
          "body": "Spread hydration throughout the day. Gulping water all at once is far less effective than consistent sipping.",
          "meals": [
            {"time": "6:00 AM - Wake-up", "icon": "🌅", "total": "400ml", "items": [
              {"food": "💧 Warm water with lemon - replenish overnight losses", "protein": 0}
            ]},
            {"time": "8:00 AM - Before Breakfast", "icon": "☀️", "total": "500ml", "items": [
              {"food": "💧 30 min before meals - reduces appetite", "protein": 0}
            ]},
            {"time": "1:00 PM - Before Lunch", "icon": "🌤️", "total": "500ml", "items": [
              {"food": "💧 Not during or immediately after - dilutes enzymes", "protein": 0}
            ]},
            {"time": "4:00 PM - Afternoon", "icon": "🥥", "total": "400ml", "items": [
              {"food": "🥥 Coconut water or nimbu pani - beats 3pm energy dip", "protein": 0}
            ]},
            {"time": "7:00 PM - Before Dinner", "icon": "🌙", "total": "500ml", "items": [
              {"food": "💧 Reduces evening overeating significantly", "protein": 0}
            ]}
          ],
          "daily_total": "~2.8 litres (drinks only) ✓"}},
        {"card_id": "hyd_10", "number": "10", "label": "Summary", "icon": "✅",
         "title": "Your Hydration Cheat Sheet", "order": 10,
         "content": {"type": "summary",
          "takeaways": [
            "By the time you feel thirsty, you're already 1-2% dehydrated - enough to impair thinking and performance",
            "The '8 glasses' rule is a myth - real needs = body weight x 35ml + adjustments for heat and exercise",
            "Check urine colour daily - pale yellow means hydrated. Dark yellow or brown means drink immediately",
            "Tea and coffee are mildly dehydrating in excess - don't rely on chai for hydration",
            "Thirst is often mistaken for hunger - drink water before snacking and wait 15 minutes",
            "Coconut water, chaas and nimbu pani are superior to commercial sports drinks for Indian conditions",
            "Drinking 500ml before each meal reduces calorie intake by 13% - the easiest weight management tool"
          ],
          "targets": [
            {"who": "🪑 Sedentary Adult", "amount": "2.0-2.5L/day"},
            {"who": "🏃 Active Adult", "amount": "3.0-3.5L/day"},
            {"who": "🌡️ Indian Summer", "amount": "Add 500-1000ml"},
            {"who": "🤰 Pregnant Women", "amount": "+300ml above normal"},
            {"who": "🏋️ Heavy Exercise", "amount": "+500ml per hour"}
          ]}},
        {"card_id": "hyd_checklist", "number": "11", "label": "Action Checklist", "icon": "📋",
         "title": "Your Action Plan", "order": 11,
         "content": {"type": "checklist",
          "body": "Start today - hydration changes take effect immediately.",
          "checklist": [
            "Start every morning with 400ml water before tea or coffee",
            "Drink 500ml water 30 minutes before every meal",
            "Keep a 1-litre water bottle visible at your desk - you drink what you see",
            "Check urine colour every morning - aim for pale yellow",
            "Replace afternoon chai with coconut water or nimbu pani in summer",
            "Next time you feel a snack craving, drink a full glass of water first and wait 15 minutes",
            "Never drink fewer than 2 litres on any day - even in winter or on rest days"
          ]}}
    ]
}

async def add_new_topics():
    for topic in [FIBRE_TOPIC, VITAMINS_TOPIC, HYDRATION_TOPIC]:
        existing = await db.topics.find_one({"key": topic["key"]})
        if existing:
            print(f"Topic '{topic['key']}' already exists, updating...")
            await db.topics.replace_one({"key": topic["key"]}, topic)
        else:
            await db.topics.insert_one(topic)
            print(f"Added new topic: {topic['key']} ({topic['card_count']} cards)")

    count = await db.topics.count_documents({})
    print(f"\nTotal topics in database: {count}")

asyncio.run(add_new_topics())
client.close()
