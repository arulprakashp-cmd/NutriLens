# NutriLens - Product Requirements Document

## Overview
A mobile nutrition education app (renamed from "Know Your Food") that presents information about six essential nutrient topics through beautifully designed, swipeable cards. Built for Indian audiences with culturally relevant food sources and dietary recommendations.

## Core Features
- **Home Screen**: Overview of 6 nutrition topics with colorful themed cards
- **Stack Navigation**: Home + Language tabs, topics open in full-screen stack screens
- **Swipeable Cards**: Horizontal card swiping with progress indicator
- **Rich Content Types**: 25+ card type renderers (stats, benefits, timelines, GI charts, food bars, meal plans, myths, etc.)
- **Share Feature**: Image-based sharing (react-native-view-shot) with text+link fallback
- **NutriLens Branding**: Watermark on cards for shared screenshots
- **MongoDB Storage**: Content stored in database for easy expansion
- **Multi-language**: English, Tamil, Hindi support (UI labels translated)

## Topics (6 total, 72 cards)
- **Protein Story**: 10 cards - protein gap, amino acids, daily targets, Indian sources, meal plans
- **Carbs Story**: 13 cards - GI index, millet myth, diabetes risk, sugar truth, smart swaps
- **Fats Story**: 14 cards - myths busted, fat types, trans fat, cholesterol, cooking oils
- **Fibre Story**: 11 cards - gut health, weight loss, disease prevention, Indian sources
- **Vitamins & Minerals Story**: 13 cards - D, B12, Iron, Calcium, Zinc, supplement guide
- **Hydration Story**: 11 cards - water needs, electrolytes, traditional Indian drinks

## Tech Stack
- **Frontend**: React Native (Expo SDK 54) with expo-router
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Navigation**: Bottom tabs (Home + Language) + Stack screens for topics
- **Sharing**: react-native-view-shot + expo-sharing
- **i18n**: Custom translation system with Language context

## API Endpoints
- `GET /api/topics` - List all topics
- `GET /api/topics/{key}` - Get topic with all cards
- `GET /api/cards/{card_id}` - Get individual card
- `GET /api/share/{card_id}` - Get formatted share data

## Multi-language Support
- UI labels: Fully translated (English, Tamil, Hindi) via i18n.ts
- Card content: Fully translated titles and body text for all 72 cards in Tamil and Hindi, stored in MongoDB `translations` field
- Topic-level translations: Topic titles, subtitles, descriptions translated
- Language selection: Persisted via AsyncStorage
- Frontend: NutrientCard reads `card.translations[lang].title/body` with English fallback
