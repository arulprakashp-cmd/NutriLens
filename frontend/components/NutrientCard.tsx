import React, { useRef, useCallback } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Share, Alert, Platform } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { captureRef } from 'react-native-view-shot';
import * as FileSystem from 'expo-file-system';
import * as Sharing from 'expo-sharing';
import { Card as CardType } from '../types';
import { api } from '../utils/api';
import { useLanguage } from '../utils/LanguageContext';
import { Language } from '../utils/i18n';
import {
  AminoAcidsRenderer, ProteinPlanRenderer, FoodBarsRenderer,
  MealPlanRenderer, GIScaleRenderer, GIChartRenderer,
  SugarComparisonRenderer, SwapsRenderer, TargetsRenderer,
  TimelineRenderer, FatRolesRenderer, FatTypesRenderer,
  SaturationChartRenderer, MythsRenderer, OmegaBalanceRenderer,
  CholesterolRenderer, CookingOilsRenderer, FatTargetsRenderer,
} from './CardRenderers';

const APP_LINK = 'https://nutrilens.app';

interface NutrientCardProps {
  card: CardType;
  backgroundColor: string;
  currentIndex: number;
  totalCards: number;
}

export default function NutrientCard({ card, backgroundColor, currentIndex, totalCards }: NutrientCardProps) {
  const cardRef = useRef<View>(null);
  const { language } = useLanguage();

  // Get translated title and body
  const cardTitle = (language !== 'en' && card.translations?.[language]?.title) || card.title;
  const cardBody = (language !== 'en' && card.translations?.[language]?.body) || card.content.body;
  const translatedContent = { ...card.content, body: cardBody };

  const handleShare = useCallback(async () => {
    try {
      // Try image-based sharing first
      if (cardRef.current) {
        try {
          const uri = await captureRef(cardRef, {
            format: 'png',
            quality: 0.85,
          });

          const isAvailable = await Sharing.isAvailableAsync();
          if (isAvailable && uri) {
            // On native: use expo-sharing for image
            await Sharing.shareAsync(uri, {
              mimeType: 'image/png',
              dialogTitle: 'Share this nutrition card',
            });
            return;
          }
        } catch (imgErr) {
          // Image capture failed, fall back to text
          console.log('Image share fallback to text');
        }
      }

      // Fallback: text-based share with formatted content + app link
      const shareData = await api.getShareCard(card.card_id);
      await Share.share({
        message: `${shareData.topic_title}\n\n${card.icon} ${shareData.card_number}\n${shareData.card_title}\n\n${shareData.content_text}\n\nLearn more: ${APP_LINK}`,
        title: shareData.card_title,
      });
    } catch (error: any) {
      if (error?.message !== 'Share cancelled' && error?.message !== 'User did not share') {
        Alert.alert('Share', 'Could not share this card');
      }
    }
  }, [card]);

  const renderContent = () => {
    const { type } = translatedContent;
    switch (type) {
      case 'stats': return <StatsRenderer content={translatedContent} />;
      case 'benefits': return <BenefitsRenderer content={translatedContent} />;
      case 'process': return <ProcessRenderer content={translatedContent} />;
      case 'comparison': return <ComparisonRenderer content={translatedContent} />;
      case 'split_comparison': return <SplitComparisonRenderer content={translatedContent} />;
      case 'summary': return <SummaryRenderer content={translatedContent} />;
      case 'amino_acids': return <AminoAcidsRenderer content={translatedContent} />;
      case 'protein_plan': return <ProteinPlanRenderer content={translatedContent} />;
      case 'protein_bars': return <FoodBarsRenderer content={translatedContent} />;
      case 'fat_bars': return <FoodBarsRenderer content={translatedContent} />;
      case 'meal_plan': return <MealPlanRenderer content={translatedContent} />;
      case 'gi_scale': return <GIScaleRenderer content={translatedContent} />;
      case 'gi_chart': return <GIChartRenderer content={translatedContent} />;
      case 'sugar_comparison': return <SugarComparisonRenderer content={translatedContent} />;
      case 'swaps': return <SwapsRenderer content={translatedContent} />;
      case 'targets': return <TargetsRenderer content={translatedContent} />;
      case 'timeline': return <TimelineRenderer content={translatedContent} />;
      case 'fat_roles': return <FatRolesRenderer content={translatedContent} />;
      case 'fat_types': return <FatTypesRenderer content={translatedContent} />;
      case 'saturation_chart': return <SaturationChartRenderer content={translatedContent} />;
      case 'myths': return <MythsRenderer content={translatedContent} />;
      case 'omega_balance': return <OmegaBalanceRenderer content={translatedContent} />;
      case 'cholesterol': return <CholesterolRenderer content={translatedContent} />;
      case 'cooking_oils': return <CookingOilsRenderer content={translatedContent} />;
      case 'fat_targets': return <FatTargetsRenderer content={translatedContent} />;
      case 'checklist': return <ChecklistRenderer content={translatedContent} />;
      default: return <DefaultRenderer content={translatedContent} />;
    }
  };

  return (
    <View style={[styles.cardContainer, { backgroundColor }]} testID={`card-${card.card_id}`}>
      <ScrollView
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.scrollContent}
      >
        <View ref={cardRef} collapsable={false} style={styles.card}>
          {/* Card Header */}
          <View style={styles.cardHeader}>
            <View style={styles.chipContainer}>
              <Text style={styles.cardNumber}>{card.number} / {card.label}</Text>
            </View>
            <TouchableOpacity testID={`share-btn-${card.card_id}`} onPress={handleShare} style={styles.shareButton} activeOpacity={0.7}>
              <Ionicons name="share-social-outline" size={22} color="#C8441A" />
            </TouchableOpacity>
          </View>

          {/* Card Icon + Title Row */}
          <View style={styles.cardTitleRow}>
            <Text style={styles.cardIconLarge}>{card.icon}</Text>
            <Text style={styles.cardTitle}>{cardTitle}</Text>
          </View>

          {/* Dynamic Content */}
          <View style={styles.cardBody}>
            {renderContent()}
          </View>

          {/* Progress Bar - pushed to bottom */}
          <View style={styles.progressContainer}>
            <View style={styles.progressBar}>
              <View style={[styles.progressFill, { width: `${((currentIndex + 1) / totalCards) * 100}%` }]} />
            </View>
            <Text style={styles.progressText}>
              {currentIndex + 1} of {totalCards}
            </Text>
          </View>

          {/* App branding for screenshots */}
          <View style={styles.brandingRow}>
            <Ionicons name="leaf" size={12} color="#4CAF50" />
            <Text style={styles.brandingText}>Know Your Food</Text>
          </View>
        </View>
      </ScrollView>
    </View>
  );
}

// ========== INLINE BASIC RENDERERS ==========

function DefaultRenderer({ content }: { content: any }) {
  return content.body ? <Text style={bs.body}>{content.body}</Text> : null;
}

function StatsRenderer({ content }: { content: any }) {
  const accentColors = ['#C8441A', '#1A7A6E', '#B8860B'];
  return (
    <>
      <Text style={bs.body}>{content.body}</Text>
      <View style={bs.statsGrid}>
        {content.stats?.map((stat: any, i: number) => (
          <View key={i} style={[bs.statBox, { borderLeftColor: accentColors[i % 3] }]}>
            <Text style={[bs.statValue, { color: accentColors[i % 3] }]}>{stat.value}</Text>
            <Text style={bs.statLabel}>{stat.label}</Text>
          </View>
        ))}
      </View>
    </>
  );
}

function BenefitsRenderer({ content }: { content: any }) {
  const bgColors = ['#FFF0E8', '#E8F5E9', '#FFF8E1', '#E3F2FD'];
  return (
    <>
      <Text style={bs.body}>{content.body}</Text>
      <View style={{ gap: 10 }}>
        {content.benefits?.map((b: any, i: number) => (
          <View key={i} style={[bs.benefitItem, { backgroundColor: bgColors[i % 4] }]}>
            <View style={bs.benefitIconWrap}><Text style={bs.benefitIcon}>{b.icon}</Text></View>
            <View style={{ flex: 1 }}>
              <Text style={bs.benefitTitle}>{b.title}</Text>
              <Text style={bs.benefitDesc}>{b.description}</Text>
            </View>
          </View>
        ))}
      </View>
      {content.callout && (
        <View style={bs.callout}><Text style={bs.calloutText}>{content.callout}</Text></View>
      )}
    </>
  );
}

function ProcessRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={bs.body}>{content.body}</Text>
      <View style={{ gap: 4 }}>
        {content.steps?.map((step: any, i: number) => (
          <View key={i} style={bs.processRow}>
            <View style={bs.processLeft}>
              <View style={bs.stepCircle}><Text style={bs.stepNum}>{step.number}</Text></View>
              {i < content.steps.length - 1 && <View style={bs.stepLine} />}
            </View>
            <View style={bs.processContent}>
              <Text style={bs.processTitle}>{step.title}</Text>
              <Text style={bs.processDesc}>{step.description}</Text>
            </View>
          </View>
        ))}
      </View>
      {content.callout && (
        <View style={bs.callout}><Text style={bs.calloutText}>{content.callout}</Text></View>
      )}
      {content.hidden_sources && (
        <View style={{ marginTop: 12 }}>
          <Text style={bs.body}>Where it hides in India:</Text>
          <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
            {content.hidden_sources.map((s: string, i: number) => (
              <View key={i} style={bs.villainTag}><Text style={bs.villainText}>{s}</Text></View>
            ))}
          </View>
        </View>
      )}
    </>
  );
}

function ComparisonRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={bs.body}>{content.body}</Text>
      {content.macros && (
        <View style={{ gap: 12 }}>
          {content.macros.map((m: any, i: number) => (
            <View key={i}>
              <View style={bs.macroRow}><Text style={bs.macroName}>{m.name}</Text><Text style={[bs.macroKcal, { color: m.color }]}>{m.kcal} kcal/g</Text></View>
              <View style={bs.macroTrack}><View style={[bs.macroFill, { width: `${(m.kcal / 9) * 100}%`, backgroundColor: m.color }]} /></View>
            </View>
          ))}
        </View>
      )}
      {content.callout && (
        <View style={bs.callout}><Text style={bs.calloutText}>{content.callout}</Text></View>
      )}
    </>
  );
}

function SplitComparisonRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={bs.body}>{content.body}</Text>
      <View style={bs.splitRow}>
        <View style={bs.splitCol}>
          <View style={[bs.splitHead, { backgroundColor: '#E8F5E9' }]}><Text style={bs.splitHeadText}>✅ Good Carbs</Text></View>
          {content.good?.map((item: string, i: number) => (
            <Text key={i} style={bs.splitItem}>{item}</Text>
          ))}
        </View>
        <View style={bs.splitCol}>
          <View style={[bs.splitHead, { backgroundColor: '#FFEBEE' }]}><Text style={bs.splitHeadText}>❌ Bad Carbs</Text></View>
          {content.bad?.map((item: string, i: number) => (
            <Text key={i} style={bs.splitItem}>{item}</Text>
          ))}
        </View>
      </View>
      {content.tip && (
        <View style={[bs.callout, { backgroundColor: '#E3F2FD', borderLeftColor: '#2196F3' }]}>
          <Text style={bs.calloutText}>{content.tip}</Text>
        </View>
      )}
    </>
  );
}

function ChecklistRenderer({ content }: { content: any }) {
  return (
    <>
      {content.body && <Text style={bs.body}>{content.body}</Text>}
      <View style={{ gap: 12 }}>
        {content.checklist?.map((item: string, i: number) => (
          <View key={i} style={bs.checkRow}>
            <View style={bs.checkBox} />
            <Text style={bs.checkText}>{item}</Text>
          </View>
        ))}
      </View>
    </>
  );
}

function SummaryRenderer({ content }: { content: any }) {
  return (
    <>
      {content.takeaways && (
        <View style={bs.summarySection}>
          <Text style={bs.summaryLabel}>💡 Key Takeaways</Text>
          {content.takeaways.map((item: string, i: number) => (
            <View key={i} style={bs.summaryItem}>
              <View style={bs.summaryDot} />
              <Text style={bs.summaryText}>{item}</Text>
            </View>
          ))}
        </View>
      )}
      {content.targets && (
        <View style={bs.summarySection}>
          <Text style={bs.summaryLabel}>🎯 Daily Targets</Text>
          <View style={bs.targetsBox}>
            {content.targets.map((t: any, i: number) => (
              <View key={i} style={bs.targetRow}>
                <Text style={bs.targetWho}>{t.who}</Text>
                <Text style={bs.targetAmt}>{t.amount}</Text>
              </View>
            ))}
          </View>
        </View>
      )}
      {content.checklist && (
        <View style={bs.summarySection}>
          <Text style={bs.summaryLabel}>✅ Action Checklist</Text>
          {content.checklist.map((item: string, i: number) => (
            <View key={i} style={bs.checkRow}>
              <View style={bs.checkBox} />
              <Text style={bs.checkText}>{item}</Text>
            </View>
          ))}
        </View>
      )}
    </>
  );
}

// ========== MAIN CARD STYLES ==========
const styles = StyleSheet.create({
  cardContainer: { flex: 1 },
  scrollContent: { flexGrow: 1, padding: 16, paddingBottom: 32 },
  card: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    borderRadius: 24,
    padding: 24,
    minHeight: 520,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08,
    shadowRadius: 16,
    elevation: 5,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  chipContainer: {
    backgroundColor: '#F5F5F5',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
  },
  cardNumber: {
    fontSize: 11,
    fontWeight: '700',
    color: '#888',
    textTransform: 'uppercase',
    letterSpacing: 1.2,
  },
  shareButton: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: '#FFF5EE',
    justifyContent: 'center',
    alignItems: 'center',
  },
  cardTitleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 14,
    marginBottom: 16,
  },
  cardIconLarge: { fontSize: 40 },
  cardTitle: {
    flex: 1,
    fontSize: 22,
    fontWeight: '800',
    color: '#1A120A',
    lineHeight: 30,
  },
  cardBody: {
    flex: 1,
  },
  progressContainer: {
    marginTop: 'auto' as any,
    paddingTop: 20,
    borderTopWidth: 1,
    borderTopColor: '#F0F0F0',
    alignItems: 'center',
  },
  progressBar: {
    width: '100%',
    height: 4,
    backgroundColor: '#F0F0F0',
    borderRadius: 2,
    overflow: 'hidden',
    marginBottom: 8,
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#C8441A',
    borderRadius: 2,
  },
  progressText: {
    fontSize: 12,
    color: '#888',
    fontWeight: '600',
  },
  brandingRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    marginTop: 10,
  },
  brandingText: {
    fontSize: 11,
    color: '#AAA',
    fontWeight: '600',
  },
});

// ========== BASIC RENDERER STYLES ==========
const bs = StyleSheet.create({
  body: { fontSize: 15, lineHeight: 23, color: '#444', marginBottom: 16 },
  // Stats
  statsGrid: { gap: 10 },
  statBox: { backgroundColor: '#FAFAFA', borderRadius: 14, padding: 16, borderLeftWidth: 4 },
  statValue: { fontSize: 32, fontWeight: '800' },
  statLabel: { fontSize: 13, color: '#666', lineHeight: 19, marginTop: 4 },
  // Benefits
  benefitItem: { flexDirection: 'row', gap: 12, borderRadius: 14, padding: 14 },
  benefitIconWrap: { width: 44, height: 44, borderRadius: 22, backgroundColor: 'rgba(255,255,255,0.8)', justifyContent: 'center', alignItems: 'center' },
  benefitIcon: { fontSize: 22 },
  benefitTitle: { fontSize: 15, fontWeight: '700', color: '#1A120A', marginBottom: 2 },
  benefitDesc: { fontSize: 13, color: '#555', lineHeight: 19 },
  callout: { backgroundColor: '#FFF8E1', borderLeftWidth: 4, borderLeftColor: '#F0A060', borderRadius: 10, padding: 14, marginTop: 16 },
  calloutText: { fontSize: 13, color: '#444', lineHeight: 20 },
  // Process
  processRow: { flexDirection: 'row' },
  processLeft: { width: 36, alignItems: 'center' },
  stepCircle: { width: 32, height: 32, borderRadius: 16, backgroundColor: '#C8441A', justifyContent: 'center', alignItems: 'center' },
  stepNum: { fontSize: 15, fontWeight: '700', color: '#FFF' },
  stepLine: { width: 2, flex: 1, backgroundColor: '#E0E0E0', marginVertical: 4 },
  processContent: { flex: 1, paddingLeft: 12, paddingBottom: 16 },
  processTitle: { fontSize: 15, fontWeight: '700', color: '#1A120A', marginBottom: 4 },
  processDesc: { fontSize: 13, color: '#666', lineHeight: 19 },
  villainTag: { backgroundColor: '#FFEBEE', paddingHorizontal: 10, paddingVertical: 6, borderRadius: 20 },
  villainText: { fontSize: 12, color: '#C62828' },
  // Comparison
  macroRow: { flexDirection: 'row', justifyContent: 'space-between' },
  macroName: { fontSize: 14, fontWeight: '600', color: '#444' },
  macroKcal: { fontSize: 14, fontWeight: '700' },
  macroTrack: { height: 10, backgroundColor: '#F0F0F0', borderRadius: 5, overflow: 'hidden', marginTop: 6 },
  macroFill: { height: '100%', borderRadius: 5 },
  // Split
  splitRow: { flexDirection: 'row', gap: 10 },
  splitCol: { flex: 1 },
  splitHead: { padding: 10, borderRadius: 10, marginBottom: 10 },
  splitHeadText: { fontSize: 13, fontWeight: '700', color: '#1A120A', textAlign: 'center' },
  splitItem: { fontSize: 13, color: '#444', marginBottom: 6, paddingLeft: 4 },
  // Summary
  summarySection: { marginBottom: 20 },
  summaryLabel: { fontSize: 16, fontWeight: '700', color: '#1A120A', marginBottom: 12 },
  summaryItem: { flexDirection: 'row', gap: 10, marginBottom: 10 },
  summaryDot: { width: 7, height: 7, borderRadius: 4, backgroundColor: '#C8441A', marginTop: 7 },
  summaryText: { flex: 1, fontSize: 14, color: '#444', lineHeight: 21 },
  targetsBox: { backgroundColor: '#F8F8F8', borderRadius: 12, padding: 16 },
  targetRow: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 8, borderBottomWidth: 1, borderBottomColor: '#EEE' },
  targetWho: { fontSize: 14, color: '#444' },
  targetAmt: { fontSize: 14, fontWeight: '700', color: '#C8441A' },
  checkRow: { flexDirection: 'row', gap: 10, marginBottom: 10 },
  checkBox: { width: 20, height: 20, borderRadius: 4, borderWidth: 2, borderColor: '#C8441A', marginTop: 2 },
  checkText: { flex: 1, fontSize: 14, color: '#444', lineHeight: 21 },
});
