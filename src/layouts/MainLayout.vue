<template>
    <q-layout view="lhr lpR lfr"> 
        <AppNavbar/>
        <q-page-container>
            <router-view />
        </q-page-container>
        <AppFooter/>
    </q-layout>
</template>

<script setup lang="ts">
  import AppNavbar from './AppNavBar.vue';
  import AppFooter from './AppFooter.vue';
</script>
