<template>
    <q-layout view="lHh Lpr lFf">
        <AppNavbar/>
        <q-page-container>
            <router-view />
        </q-page-container>
    </q-layout>
</template>

<script setup lang="ts">
  import AppNavbar from './AppNavBar.vue';
</script>
