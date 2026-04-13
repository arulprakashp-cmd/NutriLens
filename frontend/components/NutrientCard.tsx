import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Share, Alert } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card as CardType } from '../types';
import { api } from '../utils/api';

interface NutrientCardProps {
  card: CardType;
  backgroundColor: string;
  currentIndex: number;
  totalCards: number;
}

export default function NutrientCard({ card, backgroundColor, currentIndex, totalCards }: NutrientCardProps) {
  const handleShare = async () => {
    try {
      const shareData = await api.getShareCard(card.card_id);
      await Share.share({
        message: `${shareData.topic_title}\n\n${shareData.card_number}: ${shareData.card_title}\n\n${shareData.content_text}\n\nFrom Nutrients Story App`,
      });
    } catch (error: any) {
      if (error.message !== 'Share cancelled') {
        Alert.alert('Error', 'Failed to share card');
      }
    }
  };

  const renderContent = () => {
    const { type, body } = card.content;

    switch (type) {
      case 'stats':
        return renderStatsCard();
      case 'benefits':
        return renderBenefitsCard();
      case 'process':
        return renderProcessCard();
      case 'comparison':
        return renderComparisonCard();
      case 'split_comparison':
        return renderSplitComparisonCard();
      case 'summary':
        return renderSummaryCard();
      default:
        return renderDefaultCard();
    }
  };

  const renderDefaultCard = () => (
    <>
      {card.content.body && (
        <Text style={styles.cardBody}>{card.content.body}</Text>
      )}
    </>
  );

  const renderStatsCard = () => (
    <>
      <Text style={styles.cardBody}>{card.content.body}</Text>
      <View style={styles.statsContainer}>
        {card.content.stats?.map((stat: any, index: number) => (
          <View key={index} style={styles.statBox}>
            <Text style={styles.statValue}>{stat.value}</Text>
            <Text style={styles.statLabel}>{stat.label}</Text>
          </View>
        ))}
      </View>
    </>
  );

  const renderBenefitsCard = () => (
    <>
      <Text style={styles.cardBody}>{card.content.body}</Text>
      <View style={styles.benefitsContainer}>
        {card.content.benefits?.map((benefit: any, index: number) => (
          <View key={index} style={styles.benefitItem}>
            <Text style={styles.benefitIcon}>{benefit.icon}</Text>
            <View style={styles.benefitText}>
              <Text style={styles.benefitTitle}>{benefit.title}</Text>
              <Text style={styles.benefitDescription}>{benefit.description}</Text>
            </View>
          </View>
        ))}
      </View>
      {card.content.callout && (
        <View style={styles.calloutBox}>
          <Text style={styles.calloutText}>{card.content.callout}</Text>
        </View>
      )}
    </>
  );

  const renderProcessCard = () => (
    <>
      <Text style={styles.cardBody}>{card.content.body}</Text>
      <View style={styles.processContainer}>
        {card.content.steps?.map((step: any, index: number) => (
          <View key={index} style={styles.processStep}>
            <View style={styles.stepNumber}>
              <Text style={styles.stepNumberText}>{step.number}</Text>
            </View>
            <View style={styles.stepContent}>
              <Text style={styles.stepTitle}>{step.title}</Text>
              <Text style={styles.stepDescription}>{step.description}</Text>
            </View>
          </View>
        ))}
      </View>
      {card.content.callout && (
        <View style={styles.calloutBox}>
          <Text style={styles.calloutText}>{card.content.callout}</Text>
        </View>
      )}
    </>
  );

  const renderComparisonCard = () => (
    <>
      <Text style={styles.cardBody}>{card.content.body}</Text>
      {card.content.macros && (
        <View style={styles.macrosContainer}>
          {card.content.macros.map((macro: any, index: number) => (
            <View key={index} style={styles.macroItem}>
              <View style={styles.macroHeader}>
                <Text style={styles.macroName}>{macro.name}</Text>
                <Text style={styles.macroKcal}>{macro.kcal} kcal/g</Text>
              </View>
              <View style={styles.macroBar}>
                <View style={[styles.macroBarFill, { width: `${(macro.kcal / 9) * 100}%`, backgroundColor: macro.color }]} />
              </View>
            </View>
          ))}
        </View>
      )}
      {card.content.callout && (
        <View style={styles.calloutBox}>
          <Text style={styles.calloutText}>{card.content.callout}</Text>
        </View>
      )}
    </>
  );

  const renderSplitComparisonCard = () => (
    <>
      <Text style={styles.cardBody}>{card.content.body}</Text>
      <View style={styles.splitContainer}>
        <View style={styles.splitColumn}>
          <View style={[styles.splitHeader, styles.splitHeaderGood]}>
            <Text style={styles.splitHeaderText}>✅ Good Carbs</Text>
          </View>
          {card.content.good?.map((item: string, index: number) => (
            <Text key={index} style={styles.splitItem}>{item}</Text>
          ))}
        </View>
        <View style={styles.splitColumn}>
          <View style={[styles.splitHeader, styles.splitHeaderBad]}>
            <Text style={styles.splitHeaderText}>❌ Bad Carbs</Text>
          </View>
          {card.content.bad?.map((item: string, index: number) => (
            <Text key={index} style={styles.splitItem}>{item}</Text>
          ))}
        </View>
      </View>
      {card.content.tip && (
        <View style={styles.tipBox}>
          <Text style={styles.tipText}>{card.content.tip}</Text>
        </View>
      )}
    </>
  );

  const renderSummaryCard = () => (
    <>
      {card.content.takeaways && (
        <View style={styles.summarySection}>
          <Text style={styles.summaryLabel}>💡 Key Takeaways</Text>
          {card.content.takeaways.map((item: string, index: number) => (
            <View key={index} style={styles.summaryItem}>
              <View style={styles.summaryDot} />
              <Text style={styles.summaryText}>{item}</Text>
            </View>
          ))}
        </View>
      )}
      
      {card.content.targets && (
        <View style={styles.summarySection}>
          <Text style={styles.summaryLabel}>🎯 Daily Targets at a Glance</Text>
          {card.content.targets.map((target: any, index: number) => (
            <View key={index} style={styles.targetRow}>
              <Text style={styles.targetWho}>{target.who}</Text>
              <Text style={styles.targetAmount}>{target.amount}</Text>
            </View>
          ))}
        </View>
      )}
      
      {card.content.checklist && (
        <View style={styles.summarySection}>
          <Text style={styles.summaryLabel}>✅ Action Checklist</Text>
          {card.content.checklist.map((item: string, index: number) => (
            <View key={index} style={styles.checklistItem}>
              <Text style={styles.checkbox}>☐</Text>
              <Text style={styles.checklistText}>{item}</Text>
            </View>
          ))}
        </View>
      )}
    </>
  );

  return (
    <View style={[styles.cardContainer, { backgroundColor }]}>
      <ScrollView 
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.scrollContent}
      >
        <View style={styles.card}>
          {/* Card Header */}
          <View style={styles.cardHeader}>
            <Text style={styles.cardNumber}>
              {card.number} / {card.label}
            </Text>
            <TouchableOpacity onPress={handleShare} style={styles.shareButton}>
              <Ionicons name="share-outline" size={20} color="#666" />
            </TouchableOpacity>
          </View>

          {/* Card Icon */}
          <Text style={styles.cardIconLarge}>{card.icon}</Text>

          {/* Card Title */}
          <Text style={styles.cardTitle}>{card.title}</Text>

          {/* Dynamic Content */}
          {renderContent()}

          {/* Progress Indicator */}
          <View style={styles.progressContainer}>
            <Text style={styles.progressText}>
              {currentIndex + 1} of {totalCards} cards
            </Text>
          </View>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  cardContainer: {
    flex: 1,
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 40,
  },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 24,
    padding: 24,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 12,
    elevation: 5,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  cardNumber: {
    fontSize: 12,
    fontWeight: '600',
    color: '#888',
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  shareButton: {
    padding: 8,
  },
  cardIconLarge: {
    fontSize: 48,
    marginBottom: 16,
  },
  cardTitle: {
    fontSize: 24,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 16,
    lineHeight: 32,
  },
  cardBody: {
    fontSize: 16,
    lineHeight: 24,
    color: '#444',
    marginBottom: 20,
  },
  // Stats Card Styles
  statsContainer: {
    gap: 12,
  },
  statBox: {
    backgroundColor: '#F8F8F8',
    borderRadius: 12,
    padding: 16,
  },
  statValue: {
    fontSize: 32,
    fontWeight: '700',
    color: '#C8441A',
    marginBottom: 4,
  },
  statLabel: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  // Benefits Card Styles
  benefitsContainer: {
    gap: 16,
  },
  benefitItem: {
    flexDirection: 'row',
    gap: 12,
  },
  benefitIcon: {
    fontSize: 24,
  },
  benefitText: {
    flex: 1,
  },
  benefitTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 4,
  },
  benefitDescription: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  calloutBox: {
    backgroundColor: '#FFF5E6',
    borderLeftWidth: 4,
    borderLeftColor: '#F0A060',
    borderRadius: 8,
    padding: 16,
    marginTop: 16,
  },
  calloutText: {
    fontSize: 14,
    color: '#444',
    lineHeight: 20,
  },
  // Process Card Styles
  processContainer: {
    gap: 16,
  },
  processStep: {
    flexDirection: 'row',
    gap: 12,
  },
  stepNumber: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: '#C8441A',
    justifyContent: 'center',
    alignItems: 'center',
  },
  stepNumberText: {
    fontSize: 16,
    fontWeight: '700',
    color: '#FFF',
  },
  stepContent: {
    flex: 1,
  },
  stepTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 4,
  },
  stepDescription: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  // Comparison Card Styles
  macrosContainer: {
    gap: 16,
  },
  macroItem: {
    gap: 8,
  },
  macroHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  macroName: {
    fontSize: 14,
    fontWeight: '600',
    color: '#444',
  },
  macroKcal: {
    fontSize: 14,
    fontWeight: '700',
    color: '#C8441A',
  },
  macroBar: {
    height: 8,
    backgroundColor: '#F0F0F0',
    borderRadius: 4,
    overflow: 'hidden',
  },
  macroBarFill: {
    height: '100%',
  },
  // Split Comparison Styles
  splitContainer: {
    flexDirection: 'row',
    gap: 12,
  },
  splitColumn: {
    flex: 1,
  },
  splitHeader: {
    padding: 12,
    borderRadius: 8,
    marginBottom: 12,
  },
  splitHeaderGood: {
    backgroundColor: '#E8F5E9',
  },
  splitHeaderBad: {
    backgroundColor: '#FFEBEE',
  },
  splitHeaderText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#1A120A',
    textAlign: 'center',
  },
  splitItem: {
    fontSize: 13,
    color: '#444',
    marginBottom: 8,
    paddingLeft: 4,
  },
  tipBox: {
    backgroundColor: '#F0F8FF',
    borderRadius: 8,
    padding: 16,
    marginTop: 16,
  },
  tipText: {
    fontSize: 14,
    color: '#444',
    lineHeight: 20,
  },
  // Summary Card Styles
  summarySection: {
    marginBottom: 24,
  },
  summaryLabel: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1A120A',
    marginBottom: 12,
  },
  summaryItem: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 12,
  },
  summaryDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#C8441A',
    marginTop: 8,
  },
  summaryText: {
    flex: 1,
    fontSize: 14,
    color: '#444',
    lineHeight: 20,
  },
  targetRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#F0F0F0',
  },
  targetWho: {
    fontSize: 14,
    color: '#444',
  },
  targetAmount: {
    fontSize: 14,
    fontWeight: '700',
    color: '#C8441A',
  },
  checklistItem: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 12,
  },
  checkbox: {
    fontSize: 16,
    color: '#888',
  },
  checklistText: {
    flex: 1,
    fontSize: 14,
    color: '#444',
    lineHeight: 20,
  },
  progressContainer: {
    marginTop: 24,
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: '#F0F0F0',
    alignItems: 'center',
  },
  progressText: {
    fontSize: 12,
    color: '#888',
    fontWeight: '600',
  },
});
