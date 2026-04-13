# Nutrients Story - Product Requirements Document

## Overview
A mobile nutrition education app that presents information about three essential macronutrients (Protein, Carbs, Fats) in beautifully designed, swipeable card format. Built for Indian audiences with culturally relevant food sources and dietary recommendations.

## Core Features
- **Home Screen**: Overview of 3 nutrition topics with colorful topic cards
- **Tab Navigation**: 4 bottom tabs (Home, Protein, Carbs, Fats) with vector icons
- **Swipeable Cards**: Horizontal card swiping with progress indicator
- **Rich Content Types**: 25+ card type renderers (stats, benefits, timelines, GI charts, food bars, meal plans, myths, etc.)
- **Share Feature**: Native share functionality for individual cards
- **MongoDB Storage**: Content stored in database for easy expansion

## Tech Stack
- **Frontend**: React Native (Expo SDK 54) with expo-router
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Navigation**: Bottom tabs via @react-navigation/bottom-tabs
- **Sharing**: expo-sharing + React Native Share API

## Content
- **Protein Story**: 9 cards (protein gap, amino acids, daily targets, Indian food sources, meal plans)
- **Carbs Story**: 12 cards (GI index, millet myth, diabetes risk, sugar truth, smart swaps)
- **Fats Story**: 13 cards (myths busted, fat types, trans fat, cholesterol, cooking oils, omega balance)

## API Endpoints
- `GET /api/topics` - List all topics
- `GET /api/topics/{key}` - Get topic with all cards
- `GET /api/cards/{card_id}` - Get individual card
- `GET /api/share/{card_id}` - Get formatted share data

## Future Enhancements
- Add more nutrition topics (Vitamins, Minerals, Water)
- User accounts with bookmarking and progress tracking
- Personalized daily targets based on user profile
- Multi-language support (Hindi, Tamil, Bengali, etc.)
- Push notifications with daily nutrition tips
- **Monetization**: Premium content packs, affiliate links to health products
