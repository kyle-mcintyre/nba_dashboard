
<template>
  <a-spin :spinning="pageLoading">
    <a-icon slot="indicator" type="loading" style="font-size: 80px" spin/>
  <div>
    <side-bar style="text-align:center">
      <template slot="links">
        <a-button type="danger" @click="searchPlayer()" style="margin-bottom:1%">Search</a-button>
        <a-auto-complete
                v-model="player"
                :data-source="dataSource"
                placeholder="search player"
                :filter-option="filterOption"
        >
        </a-auto-complete>
        <a-divider> <h3 style="color:white; margin-bottom:-2%"><b>Team:</b></h3> </a-divider>
        <h4 style="margin:-5%; color:white"> {{team}} </h4>
        <a-divider> <h3 style="color:white; margin-bottom:-2%"><b>College:</b></h3> </a-divider>
        <h4 style="margin:-5%; color:white">{{college}} </h4>
        <a-divider> <h3 style="color:white; margin-bottom:-2%"><b>Birthday:</b></h3> </a-divider>
        <h4 style="margin:-5%; color:white">{{birthday}} </h4>
        <a-divider> <h3 style="color:white; margin-bottom:-2%"><b>Height (m):</b></h3> </a-divider>
        <h4 style="margin:-5%; color:white">{{height}} </h4>
        <a-divider> <h3 style="color:white; margin-bottom:-2%"><b>Weight (kg):</b></h3> </a-divider>
        <h4 style="margin:-5%; color:white">{{weight}} </h4>
        
      </template>
    </side-bar>
    
    <a-spin :spinning="loadingState">
      <a-icon slot="indicator" type="loading" style="font-size: 80px" spin/>
      <div class="row">
        <div class="col-12">
          <card type="chart">
            <template slot="header">
              <div class="row">
                <div class="col-sm-6">
                  <h2 class="card-title">Points per Game</h2>
                  <h4>Total = {{points}}</h4>
                </div>
              </div>
            </template>
            <div class="chart-area">
              <line-chart style="height: 100%"
                          ref="bigChart"
                          chart-id="big-line-chart"
                          :chart-data="pointsChart.chartData"
                          :gradient-colors="pointsChart.gradientColors"
                          :gradient-stops="pointsChart.gradientStops"
                          :extra-options="pointsChart.extraOptions">
              </line-chart>
            </div>
          </card>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-4">
          <card type="chart">
            <template slot="header">
                  <h2 class="card-title">Rebounds per Game</h2>
                  <h4>Total = {{rebounds}}</h4>
            </template>
            <div class="chart-area">
              <line-chart style="height: 100%"
                          chart-id="purple-line-chart"
                          ref="reboundsChart"
                          :chart-data="reboundChart.chartData"
                          :gradient-colors="reboundChart.gradientColors"
                          :gradient-stops="reboundChart.gradientStops"
                          :extra-options="reboundChart.extraOptions">
              </line-chart>
            </div>
          </card>
        </div>
        <div class="col-lg-4">
          <card type="chart">
            <template slot="header">
                  <h2 class="card-title">Assists per Game</h2>
                  <h4>Total = {{assists}}</h4>
            </template>
            <div class="chart-area">
              <line-chart style="height: 100%"
                        chart-id="blue-line-chart"
                        ref="assistsChart"
                        :chart-data="assistsChart.chartData"
                        :gradient-stops="assistsChart.gradientStops"
                        :extra-options="assistsChart.extraOptions">
              </line-chart>
            </div>
          </card>
        </div>
        <div class="col-lg-4">
          <card type="chart">
            <template slot="header">
                  <h2 class="card-title">Free Throws per Game</h2>
                  <h4>Total = {{ft}}</h4>
            </template>
            <div class="chart-area">
              <line-chart style="height: 100%"
                          chart-id="freeThrowsChart"
                          ref="freeThrowsChart"
                          :chart-data="freeThrowsChart.chartData"
                          :gradient-stops="freeThrowsChart.gradientStops"
                          :extra-options="freeThrowsChart.extraOptions">
              </line-chart>
            </div>
          </card>
        </div>
      </div>
    </a-spin>

  </div>
  </a-spin>
</template>
<script>
  import LineChart from '@/components/Charts/LineChart';
  import * as chartConfigs from '@/components/Charts/config';
  import config from '@/config';
  import axios from 'axios';

  export default {
    components: {
      LineChart,
    },
    data() {
      return {
        pointsChart: {
          chartData: {
            datasets: [{ }],
            labels: [],
          },
          extraOptions: chartConfigs.greenChartOptions,
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.4, 0],
          categories: []
        },
        reboundChart: {
          extraOptions: chartConfigs.greenChartOptions,
          chartData: {
            labels: [],
            datasets: [{ }]
          },
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.2, 0],
        },
        freeThrowsChart: {
          extraOptions: chartConfigs.greenChartOptions,
          chartData: {
            labels: [],
            datasets: [{ }]
          },
          gradientColors: ['rgba(66,134,121,0.15)', 'rgba(66,134,121,0.0)', 'rgba(66,134,121,0)'],
          gradientStops: [1, 0.4, 0],
        },
        assistsChart: {
          extraOptions: chartConfigs.greenChartOptions,
          chartData: {
            labels: [],
            datasets: [{ }]
          },
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.2, 0],
        }, 
        points: '',
        rebounds:'',
        assists:'',
        ft:'', 
        player:'',
        dataSource:[], 
        team: ' - ',
        college:' - ',
        birthday:' - ',
        height:' - ',
        weight:' - ',
        loadingState: false,
        pageLoading: false,
      }
    },
    computed: {
      pointsChartCategories() {
        return this.$t('dashboard.chartCategories');
      }
    },
    methods: {
      filterOption(input, option) {
        return (
          option.componentOptions.children[0].text.toUpperCase().indexOf(input.toUpperCase()) >= 0
        );
      },

      searchPlayer(){
          this.loadingState = true
          axios.get(`http://nba-dashboard-api-dev.us-east-1.elasticbeanstalk.com/get_player_info/` + this.player)
          .then(response => {
            if(response.status == 200){
              this.team = response.data.team
              this.college = response.data.college
              this.birthday = response.data.dob
              this.height = response.data.height
              this.weight = response.data.weight
            }

          })
          .catch(e => {
            if(e.response.status == 404){
            }
            if(e.response.status == 500){
            }
          })


        axios.get(`http://nba-dashboard-api-dev.us-east-1.elasticbeanstalk.com/get_player_stats/` + this.player)
        .then(response => {
          this.points = response.data.totalPoints
          this.rebounds = response.data.totalRebounds
          this.assists = response.data.totalAssists
          this.ft = response.data.totalFT
          if(response.status == 200){
            let chartData = {
              datasets: [{
                fill: true,
                borderColor: config.colors.teal,
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: config.colors.teal,
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: config.colors.teal,
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: response.data.points
              }],
              labels: response.data.labels,
            }
              this.$refs.bigChart.updateGradients(chartData);
              this.pointsChart.chartData = chartData;

            let reboundData = {
              datasets: [{
                fill: true,
                borderColor: config.colors.primary,
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: config.colors.primary,
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: config.colors.primary,
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: response.data.reb
              }],
              labels: response.data.labels,
            }
              this.$refs.reboundsChart.updateGradients(reboundData);
              this.reboundChart.chartData = reboundData;


            let assisData = {
              datasets: [{
                fill: true,
                borderColor: config.colors.orange,
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: config.colors.orange,
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: config.colors.orange,
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: response.data.assists
              }],
              labels: response.data.labels,
            }
              this.$refs.assistsChart.updateGradients(assisData);
              this.assistsChart.chartData = assisData;

            let freeThrowData = {
              labels: response.data.labels,
              datasets: [{
                fill: true,
                borderColor: config.colors.danger,
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: config.colors.danger,
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: config.colors.danger,
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: response.data.ft,
              }]
            }
              this.$refs.freeThrowsChart.updateGradients(freeThrowData);
              this.freeThrowsChart.chartData = freeThrowData;

              this.loadingState = false
            }
        })
        .catch(e => {
          if(e.response.status == 404){
            this.loadingState = false
          }
          if(e.response.status == 500){
            this.$info({
              title: 'Internal Error',
              // JSX support
              content: (
                <div>
                <a-result status="warning" title="500" sub-title="Whoops! Looks like there's something wrong on our side :(.">
                   Make sure you've entered the players name correctly and please try again later.
                </a-result>
                </div>
              ),
            });
            this.loadingState = false
          }
        })


      }
    },
    mounted() {
      this.i18n = this.$i18n;

      axios.get(`http://nba-dashboard-api-dev.us-east-1.elasticbeanstalk.com/getPlayers`)
        .then(response => {
            this.dataSource = response.data
            this.pageLoading = false
        })
        .catch(e => {
          this.$info({
            title: 'Internal Error',
            // JSX support
            content: (
              <div>
              <a-result status="warning" title="500" sub-title="Whoops! Looks like there's something wrong on our side :(.">
                  Make sure you've entered the players name correctly and please try again later.
              </a-result>
              </div>
            ),
          });
          this.loadingPage = false
      })
    },
    beforeDestroy() {
    }
  };
</script>

