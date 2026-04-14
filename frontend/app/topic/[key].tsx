import React, { useEffect, useState, useRef } from 'react';
import { View, Text, StyleSheet, FlatList, Dimensions, ActivityIndicator, TouchableOpacity } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useLocalSearchParams, router } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { Topic } from '../../types';
import { api } from '../../utils/api';
import NutrientCard from '../../components/NutrientCard';
import { useLanguage } from '../../utils/LanguageContext';
import { t } from '../../utils/i18n';

const { width } = Dimensions.get('window');

const TOPIC_COLORS: Record<string, { bg: string; accent: string; subtitle: string }> = {
  protein: { bg: '#EDE8DF', accent: '#C8441A', subtitle: '#8B3A3A' },
  carbs: { bg: '#EDE6D6', accent: '#B8860B', subtitle: '#8B3A3A' },
  fats: { bg: '#E8E0D0', accent: '#7A1A2E', subtitle: '#8B3A3A' },
  fibre: { bg: '#E8F0E4', accent: '#2E7D32', subtitle: '#5D4037' },
  vitamins: { bg: '#E4ECF4', accent: '#1565C0', subtitle: '#5D4037' },
  hydration: { bg: '#E0F0F4', accent: '#00838F', subtitle: '#5D4037' },
};

const TOPIC_SUBTITLES: Record<string, string> = {
  protein: 'protein_subtitle',
  carbs: 'carbs_subtitle',
  fats: 'fats_subtitle',
  fibre: 'fibre_subtitle',
  vitamins: 'vitamins_subtitle',
  hydration: 'hydration_subtitle',
};

const TOPIC_KEYWORDS: Record<string, string> = {
  protein: 'protein',
  carbs: 'carbs',
  fats: 'fat',
  fibre: 'fibre',
  vitamins: 'vitamins_minerals',
  hydration: 'hydration',
};

export default function TopicScreen() {
  const { key } = useLocalSearchParams<{ key: string }>();
  const [topic, setTopic] = useState<Topic | null>(null);
  const [loading, setLoading] = useState(true);
  const flatListRef = useRef<FlatList>(null);
  const { language } = useLanguage();

  const colors = TOPIC_COLORS[key || ''] || TOPIC_COLORS.protein;
  const subtitleKey = TOPIC_SUBTITLES[key || ''] || 'protein_subtitle';
  const keywordKey = TOPIC_KEYWORDS[key || ''] || 'protein';

  useEffect(() => {
    loadTopic();
  }, [key]);

  const loadTopic = async () => {
    try {
      const data = await api.getTopic(key || '');
      setTopic(data);
    } catch (error) {
      console.error('Error loading topic:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <SafeAreaView style={[styles.loadingContainer, { backgroundColor: colors.bg }]}>
        <ActivityIndicator size="large" color={colors.accent} />
      </SafeAreaView>
    );
  }

  if (!topic) {
    return (
      <SafeAreaView style={[styles.loadingContainer, { backgroundColor: colors.bg }]}>
        <Text style={{ color: '#666' }}>Failed to load topic</Text>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={[styles.container, { backgroundColor: colors.bg }]} edges={['top']}>
      {/* Back Button + Header */}
      <View style={styles.headerRow}>
        <TouchableOpacity testID="back-btn" onPress={() => router.back()} style={styles.backButton} activeOpacity={0.7}>
          <Ionicons name="chevron-back" size={24} color="#1A120A" />
        </TouchableOpacity>
      </View>
      <View style={styles.header}>
        <Text style={styles.topicTitle}>
          {t('the', language)}{t('the', language) ? ' ' : ''}
          <Text style={[styles.topicHighlight, { color: colors.accent }]}>{t(keywordKey, language)}</Text>
          {' '}{t('story', language)}
        </Text>
        <Text style={[styles.topicSubtitle, { color: colors.subtitle }]}>{t(subtitleKey, language)}</Text>
      </View>

      {/* Cards */}
      <FlatList
        ref={flatListRef}
        data={topic.cards}
        horizontal
        pagingEnabled
        showsHorizontalScrollIndicator={false}
        renderItem={({ item, index }) => (
          <View style={styles.cardWrapper}>
            <NutrientCard
              card={item}
              backgroundColor={colors.bg}
              currentIndex={index}
              totalCards={topic.cards.length}
            />
          </View>
        )}
        keyExtractor={(item) => item.card_id}
      />

      {/* Swipe Hint */}
      <View style={styles.hintContainer}>
        <Text style={styles.hintText}>
          {'\u2190'} {t('swipe_explore', language)} {topic.card_count} {t('cards', language)} {'\u2192'}
        </Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  loadingContainer: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  headerRow: { paddingHorizontal: 12, paddingTop: 4 },
  backButton: { width: 44, height: 44, borderRadius: 22, backgroundColor: 'rgba(255,255,255,0.6)', justifyContent: 'center', alignItems: 'center' },
  header: { paddingHorizontal: 24, paddingBottom: 12, alignItems: 'center' },
  topicTitle: { fontSize: 36, fontWeight: '700', color: '#1A120A', marginBottom: 8, textAlign: 'center', fontFamily: 'serif' },
  topicHighlight: { fontFamily: 'serif' },
  topicSubtitle: { fontSize: 11, fontWeight: '600', letterSpacing: 3, textAlign: 'center' },
  cardWrapper: { width: width },
  hintContainer: { padding: 12, alignItems: 'center' },
  hintText: { fontSize: 12, color: '#888' },
});
