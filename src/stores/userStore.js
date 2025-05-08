import { reactive } from 'vue';

export const userStore = reactive({
  isLoggedIn: false,
  role: '', // 'admin' or 'user'
  email: ''
});
