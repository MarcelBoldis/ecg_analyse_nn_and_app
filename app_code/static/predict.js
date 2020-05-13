function createChart(values, values2){
    const labels = [...Array(values.length).keys()];
    data2 = [];
    for (x of values2) {
        data2.push({'x': x, 'y': values[x]})
    }

    new Chart(document.getElementById("myChart"), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    type: 'line',
                    label: 'Graf priebehu EKG Signálu',
                    borderColor: 'rgb(0,32,63)',
                    fill: false,
                    data: values,
                    pointRadius: 0
                },
                {
                    type: 'bubble',
                    label: 'Detekovaná arytmia',
                    data: data2,
                    radius: 5,
                    hoverRadius : 0,
                    backgroundColor: "rgba(245, 7, 30,1)",
                }
            ]
        },
        options: {
            scales: {
                xAxes: [{
                    gridLines: {
                        drawOnChartArea: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Časový index'
                    }
                }],
                yAxes: [{
                    gridLines: {
                        drawOnChartArea: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'EKG signál'
                    }
                }]
            }
        }
    });
}

function showTable() {
  const elem = document.getElementById("tableToShow");
    if (elem.style.display === "inline-table") {
    elem.style.display = "none";
  } else {
    elem.style.display = "inline-table";
  }
}