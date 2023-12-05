<template>
    <SectionBlock 
    title="Что вы получите после курса"
    bgClass="bg-dark"
    >
    <!-- :class="$q.screen.gt.sm ? 'col-6' : 'col-12'" -->
        <div class="q-container result">
            <div class="row">
                <div class="col-lg-4 col-md-4 col-sm-12 result__col" :class="$q.screen.gt.sm ? '' : 'text-center'">
                    <p class="result__title">Удостоверение</p>
                    <p class="result__text">Дающее право преподавать робототехнику для детей 6-12 лет в образовательных учреждениях</p>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 result__col" :class="$q.screen.gt.sm ? '' : 'text-center'">
                    <p class="result__title">Знания</p>
                    <p class="result__text">По основам разработки учебно-методических комплексов
по робототехнике и программированию</p>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 result__col" :class="$q.screen.gt.sm ? '' : 'text-center'">
                    <p class="result__title">Практику</p>
                    <p class="result__text">Возможность пройти практику по преподаванию робототехники на базе R:ED LAB (в оффлайн или онлайн формате)</p>
                </div>

            </div>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>