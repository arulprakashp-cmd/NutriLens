import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { useLanguage } from '../../utils/LanguageContext';
import { Language, t } from '../../utils/i18n';

const LANGUAGES: { code: Language; name: string; native: string; flag: string }[] = [
  { code: 'en', name: 'English', native: 'English', flag: '🇬🇧' },
  { code: 'ta', name: 'Tamil', native: 'தமிழ்', flag: '🇮🇳' },
  { code: 'hi', name: 'Hindi', native: 'हिन्दी', flag: '🇮🇳' },
];

export default function LanguageScreen() {
  const { language, setLanguage } = useLanguage();

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <View style={styles.header}>
        <Ionicons name="language" size={32} color="#C8441A" />
        <Text style={styles.title}>{t('select_language', language)}</Text>
      </View>

      <View style={styles.languageList}>
        {LANGUAGES.map((lang) => {
          const isActive = language === lang.code;
          return (
            <TouchableOpacity
              key={lang.code}
              testID={`lang-${lang.code}`}
              style={[styles.langCard, isActive && styles.langCardActive]}
              onPress={() => setLanguage(lang.code)}
              activeOpacity={0.7}
            >
              <Text style={styles.langFlag}>{lang.flag}</Text>
              <View style={styles.langInfo}>
                <Text style={[styles.langName, isActive && styles.langNameActive]}>{lang.name}</Text>
                <Text style={styles.langNative}>{lang.native}</Text>
              </View>
              {isActive && (
                <View style={styles.checkCircle}>
                  <Ionicons name="checkmark" size={18} color="#FFF" />
                </View>
              )}
            </TouchableOpacity>
          );
        })}
      </View>

      <View style={styles.noteContainer}>
        <Ionicons name="information-circle-outline" size={20} color="#888" />
        <Text style={styles.noteText}>
          Card content is currently in English. UI labels and navigation will update to your selected language.
        </Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FAF9F7' },
  header: { padding: 24, alignItems: 'center', gap: 12 },
  title: { fontSize: 24, fontWeight: '700', color: '#1A120A' },
  languageList: { paddingHorizontal: 20, gap: 12 },
  langCard: {
    flexDirection: 'row', alignItems: 'center', padding: 20,
    backgroundColor: '#FFF', borderRadius: 16, borderWidth: 2, borderColor: '#F0F0F0',
  },
  langCardActive: { borderColor: '#C8441A', backgroundColor: '#FFF5EE' },
  langFlag: { fontSize: 32, marginRight: 16 },
  langInfo: { flex: 1 },
  langName: { fontSize: 18, fontWeight: '700', color: '#1A120A', marginBottom: 2 },
  langNameActive: { color: '#C8441A' },
  langNative: { fontSize: 14, color: '#666' },
  checkCircle: { width: 32, height: 32, borderRadius: 16, backgroundColor: '#C8441A', justifyContent: 'center', alignItems: 'center' },
  noteContainer: { flexDirection: 'row', alignItems: 'flex-start', gap: 10, margin: 24, padding: 16, backgroundColor: '#F5F5F5', borderRadius: 12 },
  noteText: { flex: 1, fontSize: 13, color: '#888', lineHeight: 19 },
});
