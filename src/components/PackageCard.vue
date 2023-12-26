<template>
    <q-card class="package-card flex column justify-start q-pa-md  " :class="bgClass">

        <q-card-section class="package-card__content col">
                    <p class="package-card__title">{{ title }}</p>
                    <p class="package-card__price">{{ price }}</p>
                    <p class="package-card__details">{{ desc }}</p>
                    <q-btn no-caps name="isactive" class="package-card__btn " href="#feedback" >Оставить заявку</q-btn>
        </q-card-section>
 
    </q-card>
</template>
<script setup lang="ts">
defineProps({
    bgClass: String,
    title: String,
    desc: String,
    price: String,
   
  });

</script>