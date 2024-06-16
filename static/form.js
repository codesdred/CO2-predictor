function createChart(Xplot, yplot, typegraph){
    console.log(typegraph)
    let n = yplot.length
    for(let i=0; i<n; i++){
        if(yplot[i]<0)
            yplot[i]=0;
    }

    let plot = document.getElementById('chart')

    let myChart = new Chart(plot,{
        type: typegraph,
        data:{
            labels: Xplot,
            datasets: [{
                label: 'CO2 Emissions(tonnes)',
                data: yplot,
            }]
        },
        options:{
            responsive:true,
        },
    });

}