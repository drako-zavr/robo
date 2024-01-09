<template>
    <SectionBlock title="Что вы получите после курса" bgClass="bg-dark">
        <div class="q-container result">
            <div class="row">

                <div class="col-lg-4 col-md-4 col-sm-12 result__col">
                    <p class="result__title text-secondary">Удостоверение</p>
                    <p class="result__text text-secondary">Дающее право преподавать робототехнику для детей 6-12 лет в образовательных
                        учреждениях</p>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 result__col">
                    <p class="result__title text-secondary">Знания</p>
                    <p class="result__text text-secondary">По основам разработки учебно-методических комплексов
                        по робототехнике и программированию</p>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 result__col">
                    <div class="result_practice row">
                        <p class="result__title text-secondary text-center">Практику <span class="tooltip">При наличии свободных мест</span>
                        <img src="../assets/images/tooltip_i.svg" alt=""
                            class="tooltip-img"></p>
                    </div>
                    <p class="result__text text-secondary">Возможность пройти практику по преподаванию робототехники на базе R:ED LAB (в
                        оффлайн или онлайн формате)</p>
                </div>

            </div>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>