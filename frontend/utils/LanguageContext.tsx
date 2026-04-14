import React, { createContext, useContext, useState } from 'react';
import { Language } from '../utils/i18n';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
}

const LanguageContext = createContext<LanguageContextType>({
  language: 'en',
  setLanguage: () => {},
});

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [language, setLang] = useState<Language>('en');

  React.useEffect(() => {
    AsyncStorage.getItem('app_language').then((lang) => {
      if (lang === 'ta' || lang === 'hi') setLang(lang);
    });
  }, []);

  const setLanguage = (lang: Language) => {
    setLang(lang);
    AsyncStorage.setItem('app_language', lang);
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  return useContext(LanguageContext);
}
