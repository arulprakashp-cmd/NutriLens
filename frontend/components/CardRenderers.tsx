import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

// ========== AMINO ACIDS ==========
export function AminoAcidsRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <View style={s.aminoContainer}>
        <View style={s.aminoCluster}>
          <View style={s.aminoDotsWrap}>
            {Array.from({ length: content.essential }).map((_, i) => (
              <View key={i} style={[s.aminoDot, { backgroundColor: '#C8441A' }]} />
            ))}
          </View>
          <Text style={[s.aminoLabel, { color: '#C8441A' }]}>9 Essential{'\n'}From Food Only</Text>
        </View>
        <View style={s.aminoDivider} />
        <View style={s.aminoCluster}>
          <View style={s.aminoDotsWrap}>
            {Array.from({ length: content.non_essential }).map((_, i) => (
              <View key={i} style={[s.aminoDot, { backgroundColor: '#1A7A6E', opacity: 0.5 }]} />
            ))}
          </View>
          <Text style={[s.aminoLabel, { color: '#1A7A6E' }]}>11 Non-Essential{'\n'}Body Produces</Text>
        </View>
      </View>
      <View style={s.aminoLegend}>
        <View style={s.legendItem}>
          <View style={[s.legendDot, { backgroundColor: '#C8441A' }]} />
          <Text style={s.legendText}>Must eat daily</Text>
        </View>
        <View style={s.legendItem}>
          <View style={[s.legendDot, { backgroundColor: '#1A7A6E', opacity: 0.5 }]} />
          <Text style={s.legendText}>Body makes it</Text>
        </View>
      </View>
      {content.note && (
        <View style={[s.callout, { backgroundColor: '#FFF8E1', borderLeftColor: '#F0A060' }]}>
          <Text style={s.calloutText}>{content.note}</Text>
        </View>
      )}
    </>
  );
}

// ========== PROTEIN PLAN ==========
export function ProteinPlanRenderer({ content }: { content: any }) {
  return (
    <>
      <View style={s.intakeGrid}>
        {content.intake?.map((item: any, i: number) => (
          <View key={i} style={s.intakeBox}>
            <Text style={s.intakeEmoji}>{item.emoji}</Text>
            <Text style={s.intakeVal}>{item.value}</Text>
            <Text style={s.intakeLabel}>{item.label}</Text>
          </View>
        ))}
      </View>
      {content.sources?.complete && (
        <View style={s.sourceSection}>
          <View style={s.sourceLabelRow}>
            <Text style={s.sourceLabel}>🥇 {content.sources.complete.label}</Text>
            <View style={[s.badge, { backgroundColor: '#E8F5E9' }]}>
              <Text style={[s.badgeText, { color: '#2E7D32' }]}>{content.sources.complete.badge}</Text>
            </View>
          </View>
          <View style={s.foodTags}>
            {content.sources.complete.foods.map((food: string, i: number) => (
              <View key={i} style={[s.foodTag, { backgroundColor: '#FFF0E8' }]}>
                <Text style={s.foodTagText}>{food}</Text>
              </View>
            ))}
          </View>
        </View>
      )}
      {content.sources?.plant && (
        <View style={s.sourceSection}>
          <View style={s.sourceLabelRow}>
            <Text style={s.sourceLabel}>🌿 {content.sources.plant.label}</Text>
            <View style={[s.badge, { backgroundColor: '#E8F5E9' }]}>
              <Text style={[s.badgeText, { color: '#1A7A6E' }]}>{content.sources.plant.badge}</Text>
            </View>
          </View>
          <View style={s.foodTags}>
            {content.sources.plant.foods.map((food: string, i: number) => (
              <View key={i} style={[s.foodTag, { backgroundColor: '#E8F5E9' }]}>
                <Text style={s.foodTagText}>{food}</Text>
              </View>
            ))}
          </View>
          {content.sources.plant.note && (
            <View style={[s.callout, { backgroundColor: '#FFF8E1', borderLeftColor: '#FF9800' }]}>
              <Text style={s.calloutText}>{content.sources.plant.note}</Text>
            </View>
          )}
        </View>
      )}
    </>
  );
}

// ========== FOOD BARS (Protein/Fat per 100g) ==========
export function FoodBarsRenderer({ content }: { content: any }) {
  const colorMap: Record<string, string> = {
    'Animal Protein': '#C8441A', 'Plant Protein': '#1A7A6E', 'Nuts & Dry Fruits': '#6B8F71',
    'Animal Fats': '#7A1A2E', 'Plant Fats': '#4A5E2A', 'Nuts & Seeds': '#C9960A',
  };
  const valueKey = content.type === 'fat_bars' ? 'fat' : 'protein';
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.categories?.map((cat: any, ci: number) => {
        const barColor = colorMap[cat.name] || '#C8441A';
        const maxVal = Math.max(...cat.foods.map((f: any) => f[valueKey] || 0));
        return (
          <View key={ci} style={s.barCategory}>
            <Text style={[s.barCategoryLabel, { color: barColor }]}>{cat.emoji} {cat.name}</Text>
            {cat.foods.map((food: any, fi: number) => (
              <View key={fi} style={s.barRow}>
                <View style={s.barMeta}>
                  <Text style={s.barEmoji}>{food.emoji}</Text>
                  <Text style={s.barName} numberOfLines={1}>{food.name}</Text>
                  <Text style={[s.barValue, { color: barColor }]}>{food[valueKey]}g</Text>
                </View>
                <View style={s.barTrack}>
                  <View style={[s.barFill, { width: `${Math.min((food[valueKey] / maxVal) * 100, 100)}%`, backgroundColor: barColor }]} />
                </View>
                <Text style={s.barNote}>{food.note}</Text>
              </View>
            ))}
          </View>
        );
      })}
    </>
  );
}

// ========== MEAL PLAN ==========
export function MealPlanRenderer({ content }: { content: any }) {
  const mealColors = ['#FFF3E0', '#FFFDE7', '#F1F8E9', '#EDE7F6'];
  const mealBorders = ['#FF9800', '#FFC107', '#8BC34A', '#7E57C2'];
  const hasGrams = content.meals?.[0]?.items?.[0]?.protein !== undefined && content.meals[0].items[0].protein !== 0;
  const valueKey = hasGrams ? (content.meals?.[0]?.items?.[0]?.protein !== undefined ? 'protein' : 'fat') : null;
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.meals?.map((meal: any, i: number) => (
        <View key={i} style={[s.mealBlock, { backgroundColor: mealColors[i % 4], borderLeftColor: mealBorders[i % 4] }]}>
          <View style={s.mealHeader}>
            <Text style={s.mealIcon}>{meal.icon}</Text>
            <View>
              <Text style={s.mealTime}>{meal.time}</Text>
              <Text style={[s.mealTotal, { color: mealBorders[i % 4] }]}>{meal.total}</Text>
            </View>
          </View>
          {meal.items?.map((item: any, j: number) => (
            <View key={j} style={[s.mealItem, item.muted && s.mealItemMuted]}>
              <Text style={[s.mealFood, item.muted && s.mealFoodMuted]} numberOfLines={2}>{item.food}</Text>
              {item.tag ? (
                <View style={s.mealTag}><Text style={s.mealTagText}>{item.tag}</Text></View>
              ) : valueKey && item[valueKey] ? (
                <Text style={s.mealGrams}>{item[valueKey]}g</Text>
              ) : null}
            </View>
          ))}
        </View>
      ))}
      {content.daily_total && (
        <View style={s.dailyTotal}>
          <Text style={s.dailyTotalLabel}>🎯 Daily Total</Text>
          <Text style={s.dailyTotalValue}>{content.daily_total}</Text>
        </View>
      )}
    </>
  );
}

// ========== GI SCALE ==========
export function GIScaleRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <View style={s.giScaleBar}>
        <View style={[s.giSeg, { backgroundColor: '#5DBE7A', flex: 55 }]}><Text style={s.giSegText}>LOW</Text></View>
        <View style={[s.giSeg, { backgroundColor: '#F0A060', flex: 14 }]}><Text style={s.giSegText}>MED</Text></View>
        <View style={[s.giSeg, { backgroundColor: '#E07070', flex: 31 }]}><Text style={s.giSegText}>HIGH</Text></View>
      </View>
      <View style={s.giLabels}>
        <Text style={s.giLabelText}>0</Text>
        <Text style={s.giLabelText}>55</Text>
        <Text style={s.giLabelText}>69</Text>
        <Text style={s.giLabelText}>100</Text>
      </View>
      {content.bands?.map((band: any, i: number) => (
        <View key={i} style={s.giBand}>
          <View style={[s.giBandDot, { backgroundColor: band.color }]} />
          <View style={{ flex: 1 }}>
            <Text style={[s.giBandTitle, { color: band.color }]}>{band.level} — {band.range}</Text>
            <Text style={s.giBandDesc}>{band.description}</Text>
          </View>
        </View>
      ))}
      {content.note && (
        <View style={[s.callout, { backgroundColor: '#FFF8E1', borderLeftColor: '#FF9800' }]}>
          <Text style={s.calloutText}>{content.note}</Text>
        </View>
      )}
    </>
  );
}

// ========== GI CHART (Traffic Light) ==========
export function GIChartRenderer({ content }: { content: any }) {
  const giColor = (level: string) => level === 'high' ? '#E07070' : level === 'medium' ? '#F0A060' : '#5DBE7A';
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.foods?.map((food: any, i: number) => {
        const prevLevel = i > 0 ? content.foods[i - 1].level : food.level;
        const showSectionBreak = i === 0 || food.level !== prevLevel;
        return (
          <View key={i}>
            {showSectionBreak && (
              <Text style={[s.giSectionLabel, { color: giColor(food.level) }]}>
                {food.level === 'high' ? '🔴 HIGH GI ≥70' : food.level === 'medium' ? '🟡 MEDIUM GI 56–69' : '🟢 LOW GI ≤55'}
              </Text>
            )}
            <View style={s.giRow}>
              <Text style={s.giFoodName} numberOfLines={1}>{food.name}</Text>
              <View style={s.giBarTrack}>
                <View style={[s.giBarFill, { width: `${food.gi}%`, backgroundColor: giColor(food.level) }]} />
              </View>
              <Text style={[s.giNum, { color: giColor(food.level) }]}>{food.gi}</Text>
            </View>
          </View>
        );
      })}
      {content.millet_myth && (
        <View style={[s.callout, { backgroundColor: '#FFF3E0', borderLeftColor: '#FF9800', marginTop: 16 }]}>
          <Text style={s.calloutTitle}>{content.millet_myth.title}</Text>
          <Text style={s.calloutText}>{content.millet_myth.body}</Text>
          <View style={s.milletCompare}>
            {content.millet_myth.comparison.map((item: any, i: number) => (
              <View key={i} style={s.milletPill}>
                <Text style={s.milletName}>{item.name}</Text>
                <Text style={s.milletGI}>{item.gi}</Text>
              </View>
            ))}
          </View>
          <Text style={[s.calloutText, { marginTop: 8 }]}>{content.millet_myth.note}</Text>
        </View>
      )}
    </>
  );
}

// ========== SUGAR COMPARISON ==========
export function SugarComparisonRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <View style={s.sugarGrid}>
        {content.sugars?.map((sugar: any, i: number) => (
          <View key={i} style={s.sugarCard}>
            <Text style={s.sugarName}>{sugar.name}</Text>
            <Text style={[s.sugarGI, { color: sugar.gi >= 70 ? '#E07070' : sugar.gi >= 56 ? '#F0A060' : '#5DBE7A' }]}>GI {sugar.gi}</Text>
            <Text style={s.sugarCal}>{sugar.kcal} kcal/100g</Text>
            <View style={[s.sugarVerdictBadge, {
              backgroundColor: sugar.verdict === 'Lowest GI' ? '#E8F5E9' : sugar.verdict === 'Highest GI' ? '#FFEBEE' : '#FFF8E1',
            }]}>
              <Text style={s.sugarVerdict}>{sugar.verdict}</Text>
            </View>
          </View>
        ))}
      </View>
      {content.truth && (
        <View style={s.truthSection}>
          <Text style={[s.sectionTitle, { marginBottom: 8 }]}>💥 The Myth Busted</Text>
          {content.truth.map((item: any, i: number) => (
            <View key={i} style={s.truthRow}>
              <Text style={s.truthPoint}>{item.point}</Text>
              <Text style={s.truthDetail}>{item.detail}</Text>
            </View>
          ))}
        </View>
      )}
    </>
  );
}

// ========== SWAPS ==========
export function SwapsRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.swaps?.map((swap: any, i: number) => (
        <View key={i} style={s.swapCard}>
          <View style={s.swapFrom}>
            <Text style={s.swapLabel}>INSTEAD OF</Text>
            <Text style={s.swapFood}>{swap.from}</Text>
          </View>
          <View style={s.swapArrow}><Text style={s.swapArrowText}>→</Text></View>
          <View style={s.swapTo}>
            <Text style={s.swapLabel}>TRY THIS</Text>
            <Text style={s.swapFood}>{swap.to}</Text>
          </View>
          <View style={s.swapImpact}><Text style={s.swapImpactText}>{swap.impact}</Text></View>
        </View>
      ))}
    </>
  );
}

// ========== TARGETS ==========
export function TargetsRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.targets && (
        <View style={s.targetsContainer}>
          {content.targets.map((t: any, i: number) => (
            <View key={i} style={s.targetRow}>
              <Text style={s.targetWho}>{t.who}</Text>
              <Text style={s.targetAmt}>{t.amount}</Text>
            </View>
          ))}
        </View>
      )}
      {content.visual_guide && (
        <View style={{ marginTop: 16 }}>
          <Text style={s.sectionTitle}>📊 Carbs per Serving</Text>
          {content.visual_guide.map((item: any, i: number) => (
            <View key={i} style={s.guideRow}>
              <Text style={s.guideFood}>{item.food}</Text>
              <Text style={s.guideVal}>{item.carbs}</Text>
            </View>
          ))}
        </View>
      )}
    </>
  );
}

// ========== TIMELINE ==========
export function TimelineRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <View style={s.timelineContainer}>
        {content.events?.map((event: any, i: number) => (
          <View key={i} style={s.tlItem}>
            <View style={s.tlLeftCol}>
              <View style={s.tlDot} />
              {i < content.events.length - 1 && <View style={s.tlLine} />}
            </View>
            <View style={s.tlContent}>
              <Text style={s.tlYear}>{event.year}</Text>
              <Text style={s.tlTitle}>{event.title}</Text>
              <Text style={s.tlDesc}>{event.description}</Text>
            </View>
          </View>
        ))}
      </View>
      {content.verdict && (
        <View style={[s.callout, { backgroundColor: '#E8F5E9', borderLeftColor: '#4CAF50' }]}>
          <Text style={s.calloutText}>{content.verdict}</Text>
        </View>
      )}
    </>
  );
}

// ========== FAT ROLES ==========
export function FatRolesRenderer({ content }: { content: any }) {
  const pillColors = [{ bg: '#FFEBEE', text: '#C8441A' }, { bg: '#FFF8E1', text: '#B8860B' }, { bg: '#E3F2FD', text: '#1565C0' }];
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.macros && (
        <View style={s.macroPills}>
          {content.macros.map((m: any, i: number) => (
            <View key={i} style={[s.macroPill, { backgroundColor: pillColors[i % 3].bg }]}>
              <Text style={[s.macroPillName, { color: pillColors[i % 3].text }]}>{m.name}{m.name === 'Fat' ? ' ⭐' : ''}</Text>
              <Text style={[s.macroPillKcal, { color: pillColors[i % 3].text }]}>{m.kcal}</Text>
              <Text style={s.macroPillUnit}>kcal / g</Text>
            </View>
          ))}
        </View>
      )}
      {content.note && <Text style={[s.bodyText, { fontSize: 13, opacity: 0.7 }]}>{content.note}</Text>}
      {content.roles?.map((role: any, i: number) => (
        <View key={i} style={s.roleItem}>
          <Text style={s.roleIcon}>{role.icon}</Text>
          <View style={{ flex: 1 }}>
            <Text style={s.roleTitle}>{role.title}</Text>
            <Text style={s.roleDesc}>{role.description}</Text>
          </View>
        </View>
      ))}
    </>
  );
}

// ========== FAT TYPES ==========
export function FatTypesRenderer({ content }: { content: any }) {
  const levelColors: Record<string, { bg: string; border: string }> = {
    good1: { bg: '#E8F5E9', border: '#4CAF50' },
    good2: { bg: '#E3F2FD', border: '#2196F3' },
    warn: { bg: '#FFF8E1', border: '#FF9800' },
    bad: { bg: '#FFEBEE', border: '#F44336' },
  };
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.types?.map((type: any, i: number) => {
        const colors = levelColors[type.level] || levelColors.warn;
        return (
          <View key={i} style={[s.fatTypeCard, { backgroundColor: colors.bg, borderLeftColor: colors.border }]}>
            <Text style={s.fatTypeIcon}>{type.icon}</Text>
            <Text style={[s.fatTypeName, { color: colors.border }]}>{type.name}</Text>
            <Text style={s.fatTypeDesc}>{type.description}</Text>
            <Text style={s.fatTypeExamples}>{type.examples}</Text>
          </View>
        );
      })}
    </>
  );
}

// ========== SATURATION CHART ==========
export function SaturationChartRenderer({ content }: { content: any }) {
  const typeColor = (type: string) => type === 'plant' ? '#4A5E2A' : '#7A1A2E';
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <Text style={[s.sectionTitle, { color: '#E07070' }]}>Most Saturated → Least</Text>
      {content.fats?.map((fat: any, i: number) => (
        <View key={i} style={s.satRow}>
          <View style={s.satMeta}>
            <Text style={s.satName}>{fat.name}</Text>
            <View style={[s.satTypeBadge, { backgroundColor: fat.type === 'plant' ? '#E8F5E9' : '#FFEBEE' }]}>
              <Text style={[s.satTypeText, { color: fat.type === 'plant' ? '#2E7D32' : '#C62828' }]}>{fat.type.toUpperCase()}</Text>
            </View>
          </View>
          <View style={s.satBarTrack}>
            <View style={[s.satBarFill, {
              width: `${fat.saturation}%`,
              backgroundColor: fat.saturation > 50 ? '#E07070' : fat.saturation > 30 ? '#F0A060' : '#5DBE7A',
            }]} />
          </View>
          <Text style={[s.satVal, {
            color: fat.saturation > 50 ? '#E07070' : fat.saturation > 30 ? '#F0A060' : '#5DBE7A',
          }]}>{fat.saturation}%</Text>
        </View>
      ))}
      {content.note && (
        <View style={[s.callout, { backgroundColor: '#E8F5E9', borderLeftColor: '#4CAF50', marginTop: 16 }]}>
          <Text style={s.calloutText}>{content.note}</Text>
        </View>
      )}
    </>
  );
}

// ========== MYTHS ==========
export function MythsRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.myths?.map((myth: any, i: number) => (
        <View key={i} style={s.mythCard}>
          <View style={s.mythWrong}>
            <Text style={s.mythWrongText}>❌ "{myth.wrong}"</Text>
          </View>
          <View style={s.mythRight}>
            <Text style={s.mythRightText}>✅ {myth.right}</Text>
          </View>
        </View>
      ))}
    </>
  );
}

// ========== OMEGA BALANCE ==========
export function OmegaBalanceRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <View style={s.omegaVisual}>
        <View style={[s.omegaCol, { backgroundColor: '#E3F2FD' }]}>
          <Text style={s.omegaLabel}>Omega-3</Text>
          <Text style={[s.omegaNum, { color: '#1565C0' }]}>1</Text>
          <Text style={s.omegaSub}>{content.omega3_role}</Text>
        </View>
        <View style={s.omegaVs}>
          <Text style={s.omegaVsLabel}>IDEAL</Text>
          <Text style={[s.omegaVsValue, { color: '#4CAF50' }]}>{content.ideal_ratio}</Text>
          <Text style={s.omegaVsLabel}>ACTUAL</Text>
          <Text style={[s.omegaVsValue, { color: '#F44336' }]}>{content.actual_ratio}</Text>
        </View>
        <View style={[s.omegaCol, { backgroundColor: '#FFEBEE' }]}>
          <Text style={s.omegaLabel}>Omega-6</Text>
          <Text style={[s.omegaNum, { color: '#C62828' }]}>25</Text>
          <Text style={s.omegaSub}>{content.omega6_role}</Text>
        </View>
      </View>
      {content.info?.map((item: any, i: number) => (
        <View key={i} style={s.roleItem}>
          <Text style={s.roleIcon}>{item.icon}</Text>
          <View style={{ flex: 1 }}>
            <Text style={s.roleTitle}>{item.title}</Text>
            <Text style={s.roleDesc}>{item.description}</Text>
          </View>
        </View>
      ))}
    </>
  );
}

// ========== CHOLESTEROL ==========
export function CholesterolRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      <View style={s.liverBox}>
        <Text style={s.liverBig}>{content.liver_production}</Text>
        <View style={{ flex: 1 }}>
          <Text style={s.liverTitle}>Made by your liver</Text>
          <Text style={s.liverNote}>{content.liver_note}</Text>
        </View>
      </View>
      <View style={s.cholTypes}>
        {content.types?.map((type: any, i: number) => (
          <View key={i} style={[s.cholType, { backgroundColor: i === 0 ? '#E8F5E9' : '#FFEBEE', borderLeftColor: i === 0 ? '#4CAF50' : '#F44336' }]}>
            <Text style={[s.cholTypeName, { color: i === 0 ? '#2E7D32' : '#C62828' }]}>{type.name}</Text>
            <Text style={s.cholTypeDesc}>{type.description}</Text>
          </View>
        ))}
      </View>
      {content.egg_myth && (
        <View style={[s.callout, { backgroundColor: '#FFF8E1', borderLeftColor: '#F0A060' }]}>
          <Text style={s.calloutText}>{content.egg_myth}</Text>
        </View>
      )}
      {content.culprits && (
        <View style={{ marginTop: 12 }}>
          <Text style={s.sectionTitle}>What actually raises bad cholesterol:</Text>
          {content.culprits.map((c: any, i: number) => (
            <View key={i} style={s.culpritRow}>
              <Text style={s.culpritSource}>{c.source}</Text>
              <View style={[s.culpritBadge, {
                backgroundColor: c.impact === 'Very High' || c.impact === 'High' ? '#FFEBEE' : c.impact === 'Minimal' ? '#E8F5E9' : '#FFF8E1',
              }]}>
                <Text style={s.culpritImpact}>{c.impact}</Text>
              </View>
            </View>
          ))}
        </View>
      )}
    </>
  );
}

// ========== COOKING OILS ==========
export function CookingOilsRenderer({ content }: { content: any }) {
  const levelStyles: Record<string, { bg: string; border: string }> = {
    'High Heat': { bg: '#FFEBEE', border: '#F44336' },
    'Medium Heat': { bg: '#FFF8E1', border: '#FF9800' },
    'Cold / Finishing': { bg: '#E8F5E9', border: '#4CAF50' },
    'Avoid Completely': { bg: '#424242', border: '#212121' },
  };
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.groups?.map((group: any, i: number) => {
        const ls = levelStyles[group.level] || levelStyles['Medium Heat'];
        const isAvoid = group.level === 'Avoid Completely';
        return (
          <View key={i} style={[s.oilGroup, { backgroundColor: ls.bg, borderLeftColor: ls.border }]}>
            <View style={s.oilHeader}>
              <Text style={[s.oilLevel, isAvoid && { color: '#FFF' }]}>{group.emoji} {group.level}</Text>
              {group.temp ? <Text style={[s.oilTemp, isAvoid && { color: '#CCC' }]}>{group.temp}</Text> : null}
            </View>
            <View style={s.oilPills}>
              {group.oils.map((oil: string, j: number) => (
                <View key={j} style={[s.oilPill, isAvoid && { backgroundColor: '#616161' }]}>
                  <Text style={[s.oilPillText, isAvoid && { color: '#FFF' }]}>{oil}</Text>
                </View>
              ))}
            </View>
            <Text style={[s.oilNote, isAvoid && { color: '#EEE' }]}>{group.note}</Text>
          </View>
        );
      })}
    </>
  );
}

// ========== FAT TARGETS ==========
export function FatTargetsRenderer({ content }: { content: any }) {
  return (
    <>
      <Text style={s.bodyText}>{content.body}</Text>
      {content.example && (
        <View style={[s.callout, { backgroundColor: '#F5F5F5', borderLeftColor: '#C9960A' }]}>
          <Text style={s.calloutText}>📐 {content.example}</Text>
        </View>
      )}
      {content.targets && (
        <View style={s.targetsContainer}>
          {content.targets.map((t: any, i: number) => (
            <View key={i} style={s.targetRow}>
              <Text style={s.targetWho}>{t.who}</Text>
              <Text style={s.targetAmt}>{t.amount}</Text>
            </View>
          ))}
        </View>
      )}
      {content.common_foods && (
        <View style={{ marginTop: 16 }}>
          <Text style={s.sectionTitle}>Fat in common Indian cooking:</Text>
          <View style={s.fatFoodGrid}>
            {content.common_foods.map((item: any, i: number) => (
              <View key={i} style={s.fatFoodCell}>
                <Text style={s.fatFoodName}>{item.food}</Text>
                <Text style={s.fatFoodVal}>{item.fat}</Text>
              </View>
            ))}
          </View>
        </View>
      )}
    </>
  );
}

// ========== SHARED STYLES ==========
const s = StyleSheet.create({
  bodyText: { fontSize: 15, lineHeight: 23, color: '#444', marginBottom: 16 },
  sectionTitle: { fontSize: 15, fontWeight: '700', color: '#1A120A', marginBottom: 12 },
  callout: { borderLeftWidth: 4, borderRadius: 10, padding: 14, marginTop: 12 },
  calloutTitle: { fontSize: 14, fontWeight: '700', color: '#1A120A', marginBottom: 6 },
  calloutText: { fontSize: 13, color: '#444', lineHeight: 20 },
  // Amino Acids
  aminoContainer: { flexDirection: 'row', alignItems: 'center', backgroundColor: '#F8F8F8', borderRadius: 16, padding: 20, marginBottom: 12 },
  aminoCluster: { flex: 1, alignItems: 'center' },
  aminoDotsWrap: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'center', gap: 6, marginBottom: 8 },
  aminoDot: { width: 14, height: 14, borderRadius: 7 },
  aminoLabel: { fontSize: 12, fontWeight: '600', textAlign: 'center', lineHeight: 16 },
  aminoDivider: { width: 1, height: 60, backgroundColor: '#DDD', marginHorizontal: 12 },
  aminoLegend: { flexDirection: 'row', justifyContent: 'center', gap: 24, marginBottom: 12 },
  legendItem: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  legendDot: { width: 10, height: 10, borderRadius: 5 },
  legendText: { fontSize: 12, color: '#666' },
  // Protein Plan
  intakeGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 10, marginBottom: 16 },
  intakeBox: { width: '47%', backgroundColor: '#FFF5EE', borderRadius: 12, padding: 14, alignItems: 'center' },
  intakeEmoji: { fontSize: 28, marginBottom: 4 },
  intakeVal: { fontSize: 28, fontWeight: '700', color: '#C8441A' },
  intakeLabel: { fontSize: 12, color: '#666', textAlign: 'center' },
  sourceSection: { marginBottom: 16 },
  sourceLabelRow: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 8 },
  sourceLabel: { fontSize: 14, fontWeight: '700', color: '#1A120A' },
  badge: { paddingHorizontal: 8, paddingVertical: 3, borderRadius: 12 },
  badgeText: { fontSize: 10, fontWeight: '700' },
  foodTags: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  foodTag: { paddingHorizontal: 10, paddingVertical: 6, borderRadius: 20 },
  foodTagText: { fontSize: 13, color: '#444' },
  // Food Bars
  barCategory: { marginBottom: 16 },
  barCategoryLabel: { fontSize: 14, fontWeight: '700', marginBottom: 8 },
  barRow: { marginBottom: 10 },
  barMeta: { flexDirection: 'row', alignItems: 'center', marginBottom: 4 },
  barEmoji: { fontSize: 16, marginRight: 6 },
  barName: { flex: 1, fontSize: 13, fontWeight: '600', color: '#333' },
  barValue: { fontSize: 14, fontWeight: '700' },
  barTrack: { height: 8, backgroundColor: '#F0F0F0', borderRadius: 4, overflow: 'hidden', marginBottom: 3 },
  barFill: { height: '100%', borderRadius: 4 },
  barNote: { fontSize: 11, color: '#888', fontStyle: 'italic' },
  // Meal Plan
  mealBlock: { borderLeftWidth: 4, borderRadius: 12, padding: 14, marginBottom: 12 },
  mealHeader: { flexDirection: 'row', alignItems: 'center', gap: 10, marginBottom: 10 },
  mealIcon: { fontSize: 24 },
  mealTime: { fontSize: 15, fontWeight: '700', color: '#1A120A' },
  mealTotal: { fontSize: 13, fontWeight: '600' },
  mealItem: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingVertical: 4 },
  mealItemMuted: { opacity: 0.5 },
  mealFood: { flex: 1, fontSize: 13, color: '#444' },
  mealFoodMuted: { fontStyle: 'italic' },
  mealGrams: { fontSize: 13, fontWeight: '700', color: '#C8441A', marginLeft: 8 },
  mealTag: { backgroundColor: '#E3F2FD', paddingHorizontal: 8, paddingVertical: 3, borderRadius: 10, marginLeft: 8 },
  mealTagText: { fontSize: 11, fontWeight: '700', color: '#1565C0' },
  dailyTotal: { flexDirection: 'row', justifyContent: 'space-between', backgroundColor: '#1A120A', borderRadius: 12, padding: 16, marginTop: 8 },
  dailyTotalLabel: { fontSize: 15, fontWeight: '600', color: '#FFF' },
  dailyTotalValue: { fontSize: 15, fontWeight: '700', color: '#5DBE7A' },
  // GI Scale
  giScaleBar: { flexDirection: 'row', borderRadius: 8, overflow: 'hidden', marginBottom: 4 },
  giSeg: { height: 28, justifyContent: 'center', alignItems: 'center' },
  giSegText: { fontSize: 10, fontWeight: '700', color: '#FFF' },
  giLabels: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 16, paddingHorizontal: 2 },
  giLabelText: { fontSize: 10, color: '#888' },
  giBand: { flexDirection: 'row', alignItems: 'flex-start', gap: 10, marginBottom: 12 },
  giBandDot: { width: 12, height: 12, borderRadius: 6, marginTop: 2 },
  giBandTitle: { fontSize: 14, fontWeight: '700', marginBottom: 2 },
  giBandDesc: { fontSize: 13, color: '#666', lineHeight: 18 },
  // GI Chart
  giSectionLabel: { fontSize: 11, fontWeight: '700', letterSpacing: 1, textTransform: 'uppercase', marginTop: 12, marginBottom: 6 },
  giRow: { flexDirection: 'row', alignItems: 'center', marginBottom: 6, gap: 6 },
  giFoodName: { width: 120, fontSize: 12, color: '#444' },
  giBarTrack: { flex: 1, height: 10, backgroundColor: '#F0F0F0', borderRadius: 5, overflow: 'hidden' },
  giBarFill: { height: '100%', borderRadius: 5 },
  giNum: { width: 28, fontSize: 13, fontWeight: '700', textAlign: 'right' },
  milletCompare: { flexDirection: 'row', gap: 8, marginTop: 10 },
  milletPill: { flex: 1, backgroundColor: '#FFF', borderRadius: 8, padding: 8, alignItems: 'center' },
  milletName: { fontSize: 12, fontWeight: '600', color: '#444' },
  milletGI: { fontSize: 20, fontWeight: '700', color: '#E07070' },
  // Sugar
  sugarGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, marginBottom: 16 },
  sugarCard: { width: '47%', backgroundColor: '#F8F8F8', borderRadius: 12, padding: 12, alignItems: 'center' },
  sugarName: { fontSize: 13, fontWeight: '700', color: '#1A120A', marginBottom: 4 },
  sugarGI: { fontSize: 20, fontWeight: '700' },
  sugarCal: { fontSize: 11, color: '#888', marginBottom: 4 },
  sugarVerdictBadge: { paddingHorizontal: 8, paddingVertical: 3, borderRadius: 10 },
  sugarVerdict: { fontSize: 10, fontWeight: '700', color: '#444' },
  truthSection: { marginTop: 8 },
  truthRow: { flexDirection: 'row', gap: 8, marginBottom: 8, alignItems: 'flex-start' },
  truthPoint: { fontSize: 13, fontWeight: '600', color: '#444' },
  truthDetail: { flex: 1, fontSize: 12, color: '#666', lineHeight: 18 },
  // Swaps
  swapCard: { backgroundColor: '#F8F8F8', borderRadius: 12, overflow: 'hidden', marginBottom: 12 },
  swapFrom: { backgroundColor: '#FFEBEE', padding: 12 },
  swapTo: { backgroundColor: '#E8F5E9', padding: 12 },
  swapLabel: { fontSize: 10, fontWeight: '700', color: '#888', letterSpacing: 1, marginBottom: 2 },
  swapFood: { fontSize: 13, fontWeight: '600', color: '#444' },
  swapArrow: { alignItems: 'center', paddingVertical: 4, backgroundColor: '#F0F0F0' },
  swapArrowText: { fontSize: 16, color: '#888' },
  swapImpact: { padding: 8, alignItems: 'center', backgroundColor: '#E3F2FD' },
  swapImpactText: { fontSize: 12, fontWeight: '700', color: '#1565C0' },
  // Targets
  targetsContainer: { backgroundColor: '#F8F8F8', borderRadius: 12, padding: 16, marginBottom: 12 },
  targetRow: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 8, borderBottomWidth: 1, borderBottomColor: '#EEE' },
  targetWho: { fontSize: 14, color: '#444' },
  targetAmt: { fontSize: 14, fontWeight: '700', color: '#C8441A' },
  guideRow: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 6, borderBottomWidth: 1, borderBottomColor: '#F0F0F0' },
  guideFood: { fontSize: 13, color: '#444' },
  guideVal: { fontSize: 13, fontWeight: '700', color: '#B8860B' },
  // Timeline
  timelineContainer: { paddingLeft: 4 },
  tlItem: { flexDirection: 'row', marginBottom: 4 },
  tlLeftCol: { width: 24, alignItems: 'center' },
  tlDot: { width: 12, height: 12, borderRadius: 6, backgroundColor: '#C8441A' },
  tlLine: { width: 2, flex: 1, backgroundColor: '#DDD', marginTop: 4 },
  tlContent: { flex: 1, paddingLeft: 12, paddingBottom: 16 },
  tlYear: { fontSize: 13, fontWeight: '700', color: '#C8441A', marginBottom: 2 },
  tlTitle: { fontSize: 14, fontWeight: '700', color: '#1A120A', marginBottom: 4 },
  tlDesc: { fontSize: 13, color: '#666', lineHeight: 19 },
  // Fat Roles
  macroPills: { flexDirection: 'row', gap: 8, marginBottom: 16 },
  macroPill: { flex: 1, borderRadius: 12, padding: 12, alignItems: 'center' },
  macroPillName: { fontSize: 12, fontWeight: '700' },
  macroPillKcal: { fontSize: 28, fontWeight: '700' },
  macroPillUnit: { fontSize: 10, color: '#888' },
  roleItem: { flexDirection: 'row', gap: 12, marginBottom: 14 },
  roleIcon: { fontSize: 24 },
  roleTitle: { fontSize: 14, fontWeight: '700', color: '#1A120A', marginBottom: 2 },
  roleDesc: { fontSize: 13, color: '#666', lineHeight: 19 },
  // Fat Types
  fatTypeCard: { borderLeftWidth: 4, borderRadius: 12, padding: 14, marginBottom: 10 },
  fatTypeIcon: { fontSize: 18, marginBottom: 4 },
  fatTypeName: { fontSize: 15, fontWeight: '700', marginBottom: 4 },
  fatTypeDesc: { fontSize: 13, color: '#444', lineHeight: 19, marginBottom: 4 },
  fatTypeExamples: { fontSize: 12, color: '#888', fontStyle: 'italic' },
  // Saturation Chart
  satRow: { marginBottom: 10 },
  satMeta: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 4 },
  satName: { fontSize: 13, fontWeight: '600', color: '#444' },
  satTypeBadge: { paddingHorizontal: 6, paddingVertical: 2, borderRadius: 8 },
  satTypeText: { fontSize: 9, fontWeight: '700' },
  satBarTrack: { height: 10, backgroundColor: '#F0F0F0', borderRadius: 5, overflow: 'hidden', marginBottom: 2 },
  satBarFill: { height: '100%', borderRadius: 5 },
  satVal: { fontSize: 13, fontWeight: '700', textAlign: 'right' },
  // Myths
  mythCard: { borderRadius: 12, overflow: 'hidden', marginBottom: 12 },
  mythWrong: { backgroundColor: '#FFEBEE', padding: 12 },
  mythWrongText: { fontSize: 13, fontWeight: '600', color: '#C62828' },
  mythRight: { backgroundColor: '#E8F5E9', padding: 12 },
  mythRightText: { fontSize: 13, color: '#2E7D32', lineHeight: 19 },
  // Omega Balance
  omegaVisual: { flexDirection: 'row', alignItems: 'center', marginBottom: 16 },
  omegaCol: { flex: 1, borderRadius: 12, padding: 16, alignItems: 'center' },
  omegaLabel: { fontSize: 12, fontWeight: '700', color: '#444' },
  omegaNum: { fontSize: 36, fontWeight: '700' },
  omegaSub: { fontSize: 10, color: '#666', textAlign: 'center', lineHeight: 14 },
  omegaVs: { alignItems: 'center', paddingHorizontal: 10 },
  omegaVsLabel: { fontSize: 9, fontWeight: '700', color: '#888', letterSpacing: 1 },
  omegaVsValue: { fontSize: 16, fontWeight: '700' },
  // Cholesterol
  liverBox: { flexDirection: 'row', alignItems: 'center', gap: 14, backgroundColor: '#FFF5EE', borderRadius: 12, padding: 16, marginBottom: 16 },
  liverBig: { fontSize: 36, fontWeight: '700', color: '#C8441A' },
  liverTitle: { fontSize: 14, fontWeight: '700', color: '#1A120A', marginBottom: 4 },
  liverNote: { fontSize: 12, color: '#666', lineHeight: 18 },
  cholTypes: { gap: 10, marginBottom: 12 },
  cholType: { borderLeftWidth: 4, borderRadius: 10, padding: 14 },
  cholTypeName: { fontSize: 14, fontWeight: '700', marginBottom: 4 },
  cholTypeDesc: { fontSize: 13, color: '#444', lineHeight: 19 },
  culpritRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingVertical: 6, borderBottomWidth: 1, borderBottomColor: '#F0F0F0' },
  culpritSource: { flex: 1, fontSize: 12, color: '#444' },
  culpritBadge: { paddingHorizontal: 8, paddingVertical: 3, borderRadius: 8 },
  culpritImpact: { fontSize: 10, fontWeight: '700', color: '#444' },
  // Cooking Oils
  oilGroup: { borderLeftWidth: 4, borderRadius: 12, padding: 14, marginBottom: 12 },
  oilHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  oilLevel: { fontSize: 14, fontWeight: '700', color: '#1A120A' },
  oilTemp: { fontSize: 12, fontWeight: '600', color: '#888' },
  oilPills: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, marginBottom: 8 },
  oilPill: { backgroundColor: '#FFF', paddingHorizontal: 10, paddingVertical: 6, borderRadius: 20 },
  oilPillText: { fontSize: 12, color: '#444' },
  oilNote: { fontSize: 12, color: '#666', fontStyle: 'italic', lineHeight: 17 },
  // Fat Targets
  fatFoodGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  fatFoodCell: { width: '47%', backgroundColor: '#F8F8F8', borderRadius: 10, padding: 10 },
  fatFoodName: { fontSize: 12, color: '#666', marginBottom: 2 },
  fatFoodVal: { fontSize: 16, fontWeight: '700', color: '#C9960A' },
});
