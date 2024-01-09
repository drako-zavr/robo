<template>
    <q-card class="package-card flex column justify-start q-pa-md  " :class="bgClass">

        <q-card-section class="package-card__content col">
                    <p class="package-card__title text-center  text-h4">{{ title }}</p>
                    <p class="package-card__price text-center">{{ price }}</p>
                    <p class="package-card__details text-center">{{ desc }}</p>
                    <q-btn no-caps name="isactive" class="package-card__btn text-white bg-accent q-mx-auto" href="#feedback" >Оставить заявку</q-btn>
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