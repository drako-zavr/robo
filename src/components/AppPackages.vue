<template>
    <SectionBlock id="price" title="Выберите нужный пакет">
        <div class="q-container">
            <div class="row ">
                <div class="col-4-lg col-4-md col-12-sm centered">
                    <PackageCard 
                    title="– PRO –" 
                    price="20.000 ₽" 
                    desc="УМК по робототетхнике и программированию"
                    bgClass="package-card-active" 
                   />
                </div>
                <div class="col-4-lg col-4-md col-12-sm centered">
                    <PackageCard title="– ROBO –" price="15.000 ₽" desc="УМК по робототетхнике" />
                </div>
                <div class="col-4-lg col-4-md col-12-sm centered">
                    <PackageCard title="– PROG –" price="10.000 ₽" desc="УМК по программированию" />
                </div>
            </div>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import PackageCard from './PackageCard.vue';
import SectionBlock from './SectionBlock.vue';
</script>