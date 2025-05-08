<script setup>
import { ref } from 'vue';
import Login from './components/Login.vue';
import TicketForm from './components/TicketForm.vue';
import AccountMenu from './components/accountmenu.vue';
import TicketTable from './components/ticketTable.vue';

const isLoggedIn = ref(false);
const role = ref('');

const setUser = (user) => {
  if (user && user.role) {
    isLoggedIn.value = true;
    role.value = user.role;
  } else {
    console.warn('Invalid user object passed to setUser:', user);
  }
};


const logout = () => {
  isLoggedIn.value = false;
  role.value = '';
};

console.log(role)
</script>

<template>
  <div id="app">
    <!-- Show account menu if logged in -->
    <AccountMenu v-if="isLoggedIn" @logout="logout" />

    <!-- Show login form if not logged in -->
    <Login v-if="!isLoggedIn" @login="setUser" />

    <!-- Show ticket form if logged in but not admin -->
   <!-- Show ticket form if logged in but not admin -->
    <TicketForm v-if="isLoggedIn && role == 'user'" />


    <!-- Show ticket table if admin -->
    <TicketTable v-if="isLoggedIn && role === 'admin'" />

    <router-view />
  </div>
</template>
