<template>
    <q-card
    class="team-card flex column justify-start q-pa-md col">
    <img class="team-card__img" src="../assets/images/teacher1.jpg">
    <!-- <img class="team-card__img" src="{{ photo }}"> -->
    <q-card-section>
        <p class="team-card__name">{{name}}</p>
        <p class="team-card__position">{{position}}</p>
        <a class="team-card__details">Подробнее</a> 
    </q-card-section>
    

  
    </q-card>  
    
</template>
<script setup lang="ts">
  defineProps({
    photo: String,
    name: String,
    position: String,
    details: String
  });
</script>