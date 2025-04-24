<template>
    <div class="dashboard-container">
      <div class="risk-meter">
        <h3>Injury Risk Level</h3>
        <div class="gauge" :style="gaugeStyle">
          {{ formattedRisk }}%
        </div>
        <div class="recommendation">
          <p v-if="riskScore > 0.7" class="alert">⚠️ Reduce Training Load</p>
          <p v-else-if="riskScore > 0.4" class="warning">⚠️ Monitor Closely</p>
          <p v-else class="safe">✅ Training Load Optimal</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        riskScore: 0.0
      }
    },
    computed: {
      formattedRisk() {
        return (this.riskScore * 100).toFixed(1);
      },
      gaugeStyle() {
        return {
          '--risk-percent': `${this.formattedRisk}%`,
          'background': `conic-gradient(
            ${this.getRiskColor()} 0% ${this.formattedRisk}%,
            #eee ${this.formattedRisk}% 100%
          )`
        };
      }
    },
    methods: {
      getRiskColor() {
        if (this.riskScore > 0.7) return '#ff4444';
        if (this.riskScore > 0.4) return '#ffbb33';
        return '#00C851';
      }
    }
  }
  </script>