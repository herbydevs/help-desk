<template>
    <div class="account-menu" @click="toggleMenu">
      <div class="icon">&#9786;</div> <!-- Simple avatar icon -->
      <div v-if="showDropdown" class="dropdown">
        <a href="#" class="dropdown-item">Sign Out</a>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const showDropdown = ref(false);
  
  function toggleMenu() {
    showDropdown.value = !showDropdown.value;
  }
  </script>
  
  <style scoped>
  .account-menu {
    position: absolute;
    top: 16px;
    right: 20px;
    cursor: pointer;
    user-select: none;
  }
  
  .icon {
    background-color: #ccc;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
  }
  
  .dropdown {
    position: absolute;
    top: 45px;
    right: 0;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    min-width: 120px;
    padding: 8px 0;
    z-index: 1000;
  }
  
  .dropdown-item {
    display: block;
    padding: 10px 16px;
    text-decoration: none;
    color: #333;
    font-size: 14px;
  }
  
  .dropdown-item:hover {
    background-color: #f0f0f0;
  }
  </style>
  