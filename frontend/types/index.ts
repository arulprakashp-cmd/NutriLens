export interface TopicSummary {
  topic_id: string;
  key: string;
  title: string;
  description: string;
  icon_name: string;
  emoji: string;
  background_color: string;
  card_count: number;
  order: number;
}

export interface Card {
  card_id: string;
  number: string;
  label: string;
  icon: string;
  title: string;
  order: number;
  content: CardContent;
}

export interface CardContent {
  type: string;
  body?: string;
  [key: string]: any;
}

export interface Topic {
  topic_id: string;
  key: string;
  title: string;
  subtitle: string;
  icon_name: string;
  emoji: string;
  background_color: string;
  description: string;
  card_count: number;
  cards: Card[];
  order: number;
}
