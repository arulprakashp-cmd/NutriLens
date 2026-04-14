// Multi-language translations for NutriLens app
// Supported: English (en), Tamil (ta), Hindi (hi)

export type Language = 'en' | 'ta' | 'hi';

interface Translations {
  [key: string]: { en: string; ta: string; hi: string };
}

export const translations: Translations = {
  // App
  app_name: { en: 'NutriLens', ta: 'நியூட்ரிலென்ஸ்', hi: 'न्यूट्रीलेंस' },
  learn_about: { en: 'Learn about', ta: 'கற்றுக்கொள்ளுங்கள்', hi: 'सीखिए' },
  nutrients: { en: 'Nutrients', ta: 'ஊட்டச்சத்துகள்', hi: 'पोषक तत्व' },
  home_description: {
    en: 'Swipe through the beautifully designed cards to understand the essential nutrients better - specially built for Indian audiences.',
    ta: 'அத்தியாவசிய ஊட்டச்சத்துகளை நன்கு புரிந்து கொள்ள அழகாக வடிவமைக்கப்பட்ட அட்டைகளை ஸ்வைப் செய்யுங்கள் - இந்திய பார்வையாளர்களுக்காக சிறப்பாக உருவாக்கப்பட்டது.',
    hi: 'आवश्यक पोषक तत्वों को बेहतर ढंग से समझने के लिए खूबसूरती से डिज़ाइन किए गए कार्ड्स स्वाइप करें - भारतीय दर्शकों के लिए विशेष रूप से बनाया गया।'
  },
  swipe_hint: { en: 'Swipe cards within each story →', ta: 'ஒவ்வொரு கதையிலும் அட்டைகளை ஸ்வைப் செய்யுங்கள் →', hi: 'प्रत्येक कहानी में कार्ड स्वाइप करें →' },
  swipe_explore: { en: 'swipe to explore all', ta: 'அனைத்தையும் பார்க்க ஸ்வைப் செய்யுங்கள்', hi: 'सभी को देखने के लिए स्वाइप करें' },
  cards: { en: 'cards', ta: 'அட்டைகள்', hi: 'कार्ड' },
  of: { en: 'of', ta: 'இல்', hi: 'का' },

  // Navigation
  home: { en: 'Home', ta: 'முகப்பு', hi: 'होम' },
  language: { en: 'Language', ta: 'மொழி', hi: 'भाषा' },
  select_language: { en: 'Select Language', ta: 'மொழியைத் தேர்ந்தெடுக்கவும்', hi: 'भाषा चुनें' },

  // Topics
  the: { en: 'The', ta: '', hi: '' },
  story: { en: 'Story', ta: 'கதை', hi: 'कहानी' },
  protein: { en: 'Protein', ta: 'புரதம்', hi: 'प्रोटीन' },
  carbs: { en: 'Carbs', ta: 'கார்ப்ஸ்', hi: 'कार्ब्स' },
  fat: { en: 'Fat', ta: 'கொழுப்பு', hi: 'वसा' },
  fats: { en: 'Fats', ta: 'கொழுப்புகள்', hi: 'वसा' },
  fibre: { en: 'Fibre', ta: 'நார்ச்சத்து', hi: 'फाइबर' },
  vitamins_minerals: { en: 'Vitamins & Minerals', ta: 'வைட்டமின்கள் & தாதுக்கள்', hi: 'विटामिन और खनिज' },
  hydration: { en: 'Hydration', ta: 'நீரேற்றம்', hi: 'हाइड्रेशन' },

  // Protein subtitles
  protein_subtitle: { en: 'WHY IT MATTERS · EVERY BODY · EVERY AGE', ta: 'ஏன் முக்கியம் · ஒவ்வொரு உடலுக்கும் · ஒவ்வொரு வயதிலும்', hi: 'यह क्यों मायने रखता है · हर शरीर · हर उम्र' },
  carbs_subtitle: { en: 'FRIEND OR FOE · THE TRUTH ABOUT CARBOHYDRATES', ta: 'நண்பனா எதிரியா · கார்போஹைட்ரேட்கள் பற்றிய உண்மை', hi: 'दोस्त या दुश्मन · कार्बोहाइड्रेट का सच' },
  fats_subtitle: { en: 'THE MOST MISUNDERSTOOD MACRONUTRIENT · MYTHS BUSTED', ta: 'மிகவும் தவறாக புரிந்துகொள்ளப்பட்ட ஊட்டச்சத்து · கட்டுக்கதைகள் உடைக்கப்பட்டன', hi: 'सबसे गलत समझा गया मैक्रोन्यूट्रिएंट · मिथक तोड़े गए' },
  fibre_subtitle: { en: 'THE NUTRIENT MOST INDIANS IGNORE · MOST NEED', ta: 'பெரும்பாலான இந்தியர்கள் புறக்கணிக்கும் ஊட்டச்சத்து · மிகவும் தேவை', hi: 'अधिकांश भारतीय जिस पोषक तत्व को नज़रअंदाज़ करते हैं · सबसे ज़रूरी' },
  vitamins_subtitle: { en: 'THE MICRONUTRIENTS THAT RUN EVERYTHING', ta: 'எல்லாவற்றையும் இயக்கும் நுண்ணூட்டச்சத்துகள்', hi: 'सूक्ष्म पोषक तत्व जो सब कुछ चलाते हैं' },
  hydration_subtitle: { en: 'WATER · THE FORGOTTEN NUTRIENT · INDIA\'S CHRONIC SHORTFALL', ta: 'நீர் · மறக்கப்பட்ட ஊட்டச்சத்து · இந்தியாவின் நாள்பட்ட பற்றாக்குறை', hi: 'पानी · भूला हुआ पोषक तत्व · भारत की पुरानी कमी' },
};

export function t(key: string, lang: Language): string {
  const entry = translations[key];
  if (!entry) return key;
  return entry[lang] || entry.en;
}
