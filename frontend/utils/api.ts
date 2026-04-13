const BACKEND_URL = process.env.EXPO_PUBLIC_BACKEND_URL;

export const api = {
  async getTopics() {
    const response = await fetch(`${BACKEND_URL}/api/topics`);
    if (!response.ok) throw new Error('Failed to fetch topics');
    return response.json();
  },

  async getTopic(key: string) {
    const response = await fetch(`${BACKEND_URL}/api/topics/${key}`);
    if (!response.ok) throw new Error('Failed to fetch topic');
    return response.json();
  },

  async getCard(cardId: string) {
    const response = await fetch(`${BACKEND_URL}/api/cards/${cardId}`);
    if (!response.ok) throw new Error('Failed to fetch card');
    return response.json();
  },

  async getShareCard(cardId: string) {
    const response = await fetch(`${BACKEND_URL}/api/share/${cardId}`);
    if (!response.ok) throw new Error('Failed to create share card');
    return response.json();
  },
};
