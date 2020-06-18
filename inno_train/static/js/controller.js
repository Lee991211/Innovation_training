function gettime() {
	$.ajax({
		url: "/time",
		timeout: 10000, //超时时间设置为10秒；
		success: function(data) {
			$("#tim").html(data)
		},
		error: function(xhr, type, errorThrown) {

		}
	});
}
function get_predict_data() {
    $.ajax({
        url:"/predict",
        success: function(data) {
			ec_left1_Option.xAxis[0].data=data.ds
            ec_left1_Option.series[0].data=data.emotion_val
            // ec_left1_Option.series[1].data=data.suspect
            // ec_left1_Option.series[2].data=data.heal
            // ec_left1_Option.series[3].data=data.dead
            predict_chart.setOption(ec_left1_Option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}
// gettime()
// setInterval(gettime,1000)

