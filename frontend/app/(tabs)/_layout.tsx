import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function TabsLayout() {
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: '#C8441A',
        tabBarInactiveTintColor: '#888',
        tabBarStyle: {
          backgroundColor: '#FFF',
          borderTopWidth: 1,
          borderTopColor: '#E0E0E0',
          height: 72,
          paddingBottom: 10,
          paddingTop: 10,
        },
        tabBarLabelStyle: {
          fontSize: 13,
          fontWeight: '700',
        },
        tabBarIconStyle: {
          marginBottom: 2,
        },
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => (
            <Ionicons name="home" size={26} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="protein"
        options={{
          title: 'Protein',
          tabBarIcon: ({ color }) => (
            <Ionicons name="fitness" size={26} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="carbs"
        options={{
          title: 'Carbs',
          tabBarIcon: ({ color }) => (
            <Ionicons name="nutrition" size={26} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="fats"
        options={{
          title: 'Fats',
          tabBarIcon: ({ color }) => (
            <Ionicons name="water" size={26} color={color} />
          ),
        }}
      />
    </Tabs>
  );
}
