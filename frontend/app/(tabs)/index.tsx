import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, ActivityIndicator } from 'react-native';
import { router } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { TopicSummary } from '../../types';
import { api } from '../../utils/api';

const TOPIC_THEMES: Record<string, { gradient: string; accent: string; iconBg: string }> = {
  protein: { gradient: '#FFF0E8', accent: '#C8441A', iconBg: '#FFE0CC' },
  carbs: { gradient: '#FFF8E1', accent: '#B8860B', iconBg: '#FFE8A0' },
  fats: { gradient: '#F3EDE4', accent: '#7A1A2E', iconBg: '#F0D8C8' },
};

const TOPIC_ICONS: Record<string, string> = {
  protein: 'fitness',
  carbs: 'nutrition',
  fats: 'water',
};

export default function HomeScreen() {
  const [topics, setTopics] = useState<TopicSummary[]>([]);
  const [loading, setLoading] = useState(true);

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
    router.push(`/(tabs)/${key}` as any);
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
              <Ionicons name="leaf" size={22} color="#4CAF50" />
            </View>
            <Text style={styles.logoText}>Know Your Food</Text>
          </View>
        </View>

        {/* Hero Section */}
        <View style={styles.hero}>
          <Text style={styles.heroSubtitle}>Learn about</Text>
          <Text style={styles.heroTitle}>Nutrients</Text>
          <Text style={styles.heroDescription}>
            Swipe through the beautifully designed cards to understand the essential nutrients better - specially built for Indian audiences.
          </Text>
        </View>

        {/* Topic Cards */}
        <View style={styles.topicsContainer}>
          {topics.map((topic) => {
            const theme = TOPIC_THEMES[topic.key] || TOPIC_THEMES.protein;
            const iconName = TOPIC_ICONS[topic.key] || 'help-circle';
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
          <Text style={styles.footerText}>Swipe cards within each story →</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FAF9F7',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FAF9F7',
  },
  header: {
    paddingHorizontal: 20,
    paddingTop: 12,
    paddingBottom: 8,
  },
  logoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  logoIconWrap: {
    width: 40,
    height: 40,
    borderRadius: 12,
    backgroundColor: '#E8F5E9',
    justifyContent: 'center',
    alignItems: 'center',
  },
  logoText: {
    fontSize: 22,
    fontWeight: '800',
    color: '#1A120A',
  },
  hero: {
    paddingHorizontal: 24,
    paddingTop: 24,
    paddingBottom: 16,
  },
  heroSubtitle: {
    fontSize: 15,
    color: '#888',
    marginBottom: 4,
    fontWeight: '500',
  },
  heroTitle: {
    fontSize: 40,
    fontWeight: '800',
    color: '#1A120A',
    marginBottom: 12,
    lineHeight: 46,
  },
  heroDescription: {
    fontSize: 15,
    lineHeight: 23,
    color: '#666',
  },
  topicsContainer: {
    paddingHorizontal: 20,
    gap: 14,
  },
  topicCard: {
    flexDirection: 'row',
    borderRadius: 20,
    padding: 20,
    alignItems: 'center',
  },
  topicIconWrap: {
    width: 56,
    height: 56,
    borderRadius: 18,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 14,
  },
  topicEmoji: {
    fontSize: 28,
  },
  topicInfo: {
    flex: 1,
  },
  topicTitle: {
    fontSize: 17,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 4,
  },
  topicDescription: {
    fontSize: 13,
    color: '#666',
    lineHeight: 18,
  },
  topicArrow: {
    width: 32,
    height: 32,
    borderRadius: 16,
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 8,
  },
  footer: {
    padding: 28,
    alignItems: 'center',
  },
  footerText: {
    fontSize: 13,
    color: '#AAA',
    fontWeight: '500',
  },
});
