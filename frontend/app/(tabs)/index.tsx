import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, ActivityIndicator } from 'react-native';
import { router } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { TopicSummary } from '../../types';
import { api } from '../../utils/api';
import { useLanguage } from '../../utils/LanguageContext';
import { t } from '../../utils/i18n';

const TOPIC_THEMES: Record<string, { gradient: string; accent: string; iconBg: string }> = {
  protein: { gradient: '#FFF0E8', accent: '#C8441A', iconBg: '#FFE0CC' },
  carbs: { gradient: '#FFF8E1', accent: '#B8860B', iconBg: '#FFE8A0' },
  fats: { gradient: '#F3EDE4', accent: '#7A1A2E', iconBg: '#F0D8C8' },
  fibre: { gradient: '#E8F5E9', accent: '#2E7D32', iconBg: '#C8E6C9' },
  vitamins: { gradient: '#E3F2FD', accent: '#1565C0', iconBg: '#BBDEFB' },
  hydration: { gradient: '#E0F7FA', accent: '#00838F', iconBg: '#B2EBF2' },
};

export default function HomeScreen() {
  const [topics, setTopics] = useState<TopicSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const { language } = useLanguage();

  useEffect(() => {
    loadTopics();
  }, []);

  const loadTopics = async () => {
    try {
      const data = await api.getTopics();
      setTopics(data);
    } catch (error) {
      console.error('Error loading topics:', error);
    } finally {
      setLoading(false);
    }
  };

  const navigateToTopic = (key: string) => {
    router.push(`/topic/${key}` as any);
  };

  if (loading) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <ActivityIndicator testID="home-loader" size="large" color="#C8441A" />
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <ScrollView showsVerticalScrollIndicator={false} testID="home-scroll">
        {/* Header */}
        <View style={styles.header}>
          <View style={styles.logoContainer}>
            <View style={styles.logoIconWrap}>
              <Ionicons name="eye" size={22} color="#C8441A" />
            </View>
            <Text style={styles.logoText}>{t('app_name', language)}</Text>
          </View>
        </View>

        {/* Hero Section */}
        <View style={styles.hero}>
          <Text style={styles.heroSubtitle}>{t('learn_about', language)}</Text>
          <Text style={styles.heroTitle}>{t('nutrients', language)}</Text>
          <Text style={styles.heroDescription}>{t('home_description', language)}</Text>
        </View>

        {/* Topic Cards */}
        <View style={styles.topicsContainer}>
          {topics.map((topic) => {
            const theme = TOPIC_THEMES[topic.key] || TOPIC_THEMES.protein;
            return (
              <TouchableOpacity
                key={topic.topic_id}
                testID={`topic-card-${topic.key}`}
                style={[styles.topicCard, { backgroundColor: theme.gradient }]}
                onPress={() => navigateToTopic(topic.key)}
                activeOpacity={0.7}
              >
                <View style={[styles.topicIconWrap, { backgroundColor: theme.iconBg }]}>
                  <Text style={styles.topicEmoji}>{topic.emoji}</Text>
                </View>
                <View style={styles.topicInfo}>
                  <Text style={styles.topicTitle}>{topic.title}</Text>
                  <Text style={styles.topicDescription}>{topic.description}</Text>
                </View>
                <View style={[styles.topicArrow, { backgroundColor: theme.accent }]}>
                  <Ionicons name="chevron-forward" size={18} color="#FFF" />
                </View>
              </TouchableOpacity>
            );
          })}
        </View>

        {/* Footer */}
        <View style={styles.footer}>
          <Text style={styles.footerText}>{t('swipe_hint', language)}</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FAF9F7' },
  loadingContainer: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#FAF9F7' },
  header: { paddingHorizontal: 20, paddingTop: 12, paddingBottom: 8 },
  logoContainer: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  logoIconWrap: { width: 40, height: 40, borderRadius: 12, backgroundColor: '#FFF0E8', justifyContent: 'center', alignItems: 'center' },
  logoText: { fontSize: 24, fontWeight: '800', color: '#1A120A' },
  hero: { paddingHorizontal: 24, paddingTop: 20, paddingBottom: 12 },
  heroSubtitle: { fontSize: 15, color: '#888', marginBottom: 4, fontWeight: '500' },
  heroTitle: { fontSize: 38, fontWeight: '800', color: '#1A120A', marginBottom: 10 },
  heroDescription: { fontSize: 15, lineHeight: 23, color: '#666' },
  topicsContainer: { paddingHorizontal: 20, gap: 12 },
  topicCard: { flexDirection: 'row', borderRadius: 20, padding: 18, alignItems: 'center' },
  topicIconWrap: { width: 52, height: 52, borderRadius: 16, justifyContent: 'center', alignItems: 'center', marginRight: 14 },
  topicEmoji: { fontSize: 26 },
  topicInfo: { flex: 1 },
  topicTitle: { fontSize: 16, fontWeight: '700', color: '#1A120A', marginBottom: 3 },
  topicDescription: { fontSize: 12, color: '#666', lineHeight: 17 },
  topicArrow: { width: 30, height: 30, borderRadius: 15, justifyContent: 'center', alignItems: 'center', marginLeft: 8 },
  footer: { padding: 24, alignItems: 'center' },
  footerText: { fontSize: 13, color: '#AAA', fontWeight: '500' },
});
