<template>
    <SectionBlock
    title="Выберите нужный пакет"
    >
    <div class="q-container">
        <div class="row">
    <PackageCard/>
    <PackageCard/>
    <PackageCard/>
    </div></div>
    </SectionBlock>
</template>
<script setup lang="ts">
import PackageCard from './PackageCard.vue';
import SectionBlock from './SectionBlock.vue';
</script>