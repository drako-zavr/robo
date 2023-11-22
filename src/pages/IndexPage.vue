<template>
  <q-page class="index-page">
    <AppHeader/>
    <!-- <AppExample/> -->
    <AppTeam/>
    <AppFeedback/>
    <AppFooter/>
  </q-page>
</template>

<script setup lang="ts">
// import AppExample from 'components/AppExample.vue'
import AppFeedback from 'src/components/AppFeedback.vue';
import AppHeader from 'src/components/AppHeader.vue';
import AppTeam from 'src/components/AppTeam.vue';
import AppFooter from 'src/components/AppFooter.vue';
</script>
