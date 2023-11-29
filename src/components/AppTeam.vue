<template>
    <SectionBlock
    title="Профессиональные тренеры">
    <div class="q-container">
        <div class="row">
    <TeamCard/>
    <TeamCard/>
    <TeamCard/></div> 
    <img src="../assets/images/arrow_left.svg">
    <img src="../assets/images/arrow_right.svg">
</div>
<!-- <q-btn class="arrow-btn"></q-btn> -->

    </SectionBlock>
</template>
<script setup lang="ts">
import TeamCard from './TeamCard.vue';
import SectionBlock from './SectionBlock.vue';
</script>