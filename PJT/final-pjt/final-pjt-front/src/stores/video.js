import { defineStore } from 'pinia';

export const useVideoStore = defineStore('video', {
  state: () => ({
    showVideo: true,
    count: 0,
  }),
  actions: {
    toggleVideo() {
      this.showVideo = false;
    },
    onVideoEnded() {
      this.showVideo = false;
      this.count = 1;
    },
  },
}, {persist: true})