function drawBarGraph(id) {
  // var labels = data.labels; 
  // var chartLabel = data.chartLabel; 
  // var chartdata = data.chartdata; 
  var ctx = document.getElementById(id).getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['1', '4', '5', '7'],
      datasets: [{
        label: 'Sale',
        data: [40, 50, 44, 99],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }],
        x: {
          type: 'time',
          time: {
            displayFormat: {
              qurater: 'MMM YYY'
            }
          }
        }
      }
    }
  });
}

function drawLineGraph(data, id) {
  // var labels = data.labels; 
  // var chartLabel = data.chartLabel; 
  // var chartdata = data.chartdata; 
  var ctx = document.getElementById(id).getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.labels,
      datasets: [{
        label: 'Sales',
        data: data.amount,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
}

function drawDoughnut(data, id) {
  // var labels = data.labels; 
  // var chartLabel = data.chartLabel; 
  // var chartdata = data.chartdata; 
  var ctx = document.getElementById(id).getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: data.labels,
      datasets: [{
        label: 'Sale',
        data: data.amount,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
}


// drawLineGraph('myChartline'); 
drawBarGraph('myChartBar');
// myDoughnut


window.addEventListener('DOMContentLoaded', function (event) {
  // to prevent running funtion  twice
  if (event.isTrusted) {
    event.stopImmediatePropagation();
  }

  const apiCall = async () => {
    return await axios.get('/chartdata')
      .then(response => {
        groups = response.data.group_wise_sale

        /** @type {string[]} */
        labels = []
        /** @type {number[]} */
        amount = []

        groups.forEach(group => {
          labels.push(group.group_name)
          amount.push(group.amount)
        })

        /** @type {objects} */
        
        data = {
          labels: labels,
          amount: amount
        }

        drawLineGraph(data, 'myChartline');
        drawDoughnut(data, 'myDoughnut');
      })
      .catch(error => Promise.reject(error))
  }

  console.log(apiCall())
})
// api call

