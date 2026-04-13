import React, { useEffect, useState, useRef } from 'react';
import { View, Text, StyleSheet, FlatList, Dimensions, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Topic } from '../../types';
import { api } from '../../utils/api';
import NutrientCard from '../../components/NutrientCard';

const { width } = Dimensions.get('window');

export default function CarbsScreen() {
  const [topic, setTopic] = useState<Topic | null>(null);
  const [loading, setLoading] = useState(true);
  const [currentIndex, setCurrentIndex] = useState(0);
  const flatListRef = useRef<FlatList>(null);

  useEffect(() => {
    loadTopic();
  }, []);

  const loadTopic = async () => {
    try {
      const data = await api.getTopic('carbs');
      setTopic(data);
    } catch (error) {
      console.error('Error loading topic:', error);
    } finally {
      setLoading(false);
    }
  };

  const onViewableItemsChanged = useRef(({ viewableItems }: any) => {
    if (viewableItems.length > 0) {
      setCurrentIndex(viewableItems[0].index || 0);
    }
  }).current;

  if (loading) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#C8441A" />
      </SafeAreaView>
    );
  }

  if (!topic) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <Text>Failed to load carbs topic</Text>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.topicTitle}>The <Text style={styles.topicHighlight}>Carbs</Text> Story</Text>
        <Text style={styles.topicSubtitle}>FRIEND OR FOE · THE TRUTH ABOUT CARBOHYDRATES</Text>
      </View>

      {/* Cards */}
      <FlatList
        ref={flatListRef}
        data={topic.cards}
        horizontal
        pagingEnabled
        showsHorizontalScrollIndicator={false}
        onViewableItemsChanged={onViewableItemsChanged}
        viewabilityConfig={{
          itemVisiblePercentThreshold: 50,
        }}
        renderItem={({ item, index }) => (
          <View style={styles.cardWrapper}>
            <NutrientCard
              card={item}
              backgroundColor={topic.background_color}
              currentIndex={index}
              totalCards={topic.cards.length}
            />
          </View>
        )}
        keyExtractor={(item) => item.card_id}
      />

      {/* Swipe Hint */}
      <View style={styles.hintContainer}>
        <Text style={styles.hintText}>← swipe to explore all {topic.card_count} cards →</Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#EDE6D6',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#EDE6D6',
  },
  header: {
    padding: 20,
    paddingBottom: 12,
    alignItems: 'center',
  },
  topicTitle: {
    fontSize: 28,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 6,
    textAlign: 'center',
  },
  topicHighlight: {
    color: '#B8860B',
  },
  topicSubtitle: {
    fontSize: 12,
    color: '#8B6914',
    fontWeight: '700',
    letterSpacing: 1.5,
    textAlign: 'center',
  },
  cardWrapper: {
    width: width,
  },
  hintContainer: {
    padding: 16,
    alignItems: 'center',
  },
  hintText: {
    fontSize: 12,
    color: '#888',
  },
});
