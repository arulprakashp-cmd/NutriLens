import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, ActivityIndicator } from 'react-native';
import { router } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { TopicSummary } from '../../types';
import { api } from '../../utils/api';

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
        <ActivityIndicator size="large" color="#C8441A" />
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <ScrollView showsVerticalScrollIndicator={false}>
        {/* Header */}
        <View style={styles.header}>
          <View style={styles.logoContainer}>
            <Text style={styles.logoEmoji}>🥗</Text>
            <Text style={styles.logoText}>Nutrients Story</Text>
          </View>
        </View>

        {/* Hero Section */}
        <View style={styles.hero}>
          <Text style={styles.heroSubtitle}>Learn about</Text>
          <Text style={styles.heroTitle}>Nutrients Story</Text>
          <Text style={styles.heroDescription}>
            Swipe through beautifully designed cards about the three essential macronutrients — built for Indian audiences.
          </Text>
        </View>

        {/* Topic Cards */}
        <View style={styles.topicsContainer}>
          {topics.map((topic) => (
            <TouchableOpacity
              key={topic.topic_id}
              style={styles.topicCard}
              onPress={() => navigateToTopic(topic.key)}
              activeOpacity={0.7}
            >
              <View style={styles.topicEmoji}>
                <Text style={styles.topicEmojiText}>{topic.emoji}</Text>
              </View>
              <View style={styles.topicInfo}>
                <Text style={styles.topicTitle}>{topic.title}</Text>
                <Text style={styles.topicDescription}>{topic.description}</Text>
              </View>
              <Ionicons name="chevron-forward" size={24} color="#888" />
            </TouchableOpacity>
          ))}
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
    padding: 16,
    paddingTop: 8,
  },
  logoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  logoEmoji: {
    fontSize: 32,
  },
  logoText: {
    fontSize: 24,
    fontWeight: '700',
    color: '#1A120A',
  },
  hero: {
    padding: 24,
    paddingTop: 16,
  },
  heroSubtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 4,
  },
  heroTitle: {
    fontSize: 36,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 12,
  },
  heroDescription: {
    fontSize: 16,
    lineHeight: 24,
    color: '#555',
  },
  topicsContainer: {
    padding: 16,
    gap: 16,
  },
  topicCard: {
    flexDirection: 'row',
    backgroundColor: '#FFF',
    borderRadius: 16,
    padding: 20,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  topicEmoji: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: '#F5F5F5',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  topicEmojiText: {
    fontSize: 28,
  },
  topicInfo: {
    flex: 1,
  },
  topicTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 4,
  },
  topicDescription: {
    fontSize: 13,
    color: '#666',
    lineHeight: 18,
  },
  footer: {
    padding: 24,
    alignItems: 'center',
  },
  footerText: {
    fontSize: 14,
    color: '#888',
  },
});
