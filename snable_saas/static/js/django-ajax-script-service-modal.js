$("#get_services_modal").change(function(){
                var servicesId = $(this).val();

//        <!--        alert(countryId)-->
                // Ajax is used for that it will refresh only specific part
                $.ajax({
                    url:'get_sub_services',                  // url of the python function
                    data:{'services':servicesId},       //country is the name attribute //data is predefined dictionary object
                    success:function(data){$("#get_sub_services_id_modal").html(data);} //Select the state in the select tage based on the country id selected
                    });

            });