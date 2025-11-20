


        # Geometría del área de estudio
        # if st.session_state.aoi == "TEAPA_DEFAULT" or st.session_state.aoi is None:
        #     geometry = get_area_teapa()
        # else:
        #     # En el futuro: parsear GeoJSON cargado
        #     geometry = get_area_teapa()

        # start_date, end_date = st.session_state.date_range
        # start_date = str(start_date)
        # end_date = str(end_date)

        # # Colección Landsat 8 SR
        # collection = "LANDSAT/LC08/C02/T1_L2"

        # if "NDVI" in metricas:
        #     ndvi_layer = calcular_ndvi(collection, geometry, start_date, end_date)
        #     mapid = ndvi_layer.getMapId(
        #         {"min": 0, "max": 1, "palette": ["red", "yellow", "green"]}
        #     )
        #     folium.raster_layers.TileLayer(
        #         tiles=mapid["tile_fetcher"].url_format,
        #         attr="Google Earth Engine",
        #         name="NDVI",
        #         overlay=True,
        #         control=True,
        #     ).add_to(m)

        # if "LST" in metricas:
        #     lst_layer = calcular_lst(collection, geometry, start_date, end_date)
        #     mapid = lst_layer.getMapId(
        #         {"min": 20, "max": 40, "palette": ["blue", "yellow", "red"]}
        #     )
        #     folium.raster_layers.TileLayer(
        #         tiles=mapid["tile_fetcher"].url_format,
        #         attr="Google Earth Engine",
        #         name="LST (°C)",
        #         overlay=True,
        #         control=True,
        #     ).add_to(m)



# dem = ee.Image("USGS/SRTMGL1_003")

    # vis_params = {
    # "min": 0,
    # "max": 4000,
    # "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"]}

    # Create a map object.
    # m = geemap.Map(center=[40,-100], zoom=4)
    # m = folium.Map(location=center, zoom_start=zoom_start, control_scale=True)

    # Add the elevation model to the map object.
    # m.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, "DEM")

    # Display the map.
    # display(m)

    # Create a folium map object.

# boundaries = ee.FeatureCollection("WM/geoLab/geoBoundaries/600/ADM2")

# filtered = boundaries.filter(ee.Filter.eq("shapeName", st.session_state.locality))

# map.add_ee_layer(filtered.style(**style), {}, "ADM2 Boundaries")

GEE_PRIVATE_KEY = {"type"="service_account","project_id"= "islas-calor-teapa","private_key_id"="ec8f60e6541bac61f86be65b906e99c54513904e","private_key"= "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQC6z6f+NPi8dZp1\nXEW4mAbBswlD9igxEAljn0hQMuBxz0jRdAEHVJxQIC6KAksb22EwxLOueplEC2YP\nTr3nbryXWJFbG31zA05ib+k05CfY/1tAhsWE6U1pvFZ5nqz5pvV2Oo255NhTZTK5\nM7YKbXdLyAHuAsEVgmyuiW2jP2+nwPqE5VYDiXqdKHQoqLgUf/jAVUcxsfefnQoC\nnhoHKAL+Htx97mzC26rg13DEUo159UMHEcDiwGYIBqJ6NQL+/7/ezmRx2g0FhhAu\nckOJU8FQRDjvr+x9J5OuE0jQmuV/xAj1J1P4+Cu9keGmp6Gg7bcPPKRnLqBaClzG\nkYTPPBP/AgMBAAECgf89awhQYMS72+5sUhSaHAwcouro7S/0RtF6Gg7W+eMmMoA+\nXLqkg6zgqwlMq8mwiZqVQ2vPxtRHtXet5gre4V7KY3679Xhz180YOrLxhhGTxmC6\nAOqaSBoA1BWaPBD4A2xa8o/7Y2xmqV7ZL6cqG9NHlvpgxjG1C1cFYH7WAoUzIYNx\nszpTx0iZdcgjEZ/qQzx3SN/EixoTJrhqXgGZ+Svow7F3w3V06dTjgkuyZx38qeUl\nZLGOLsZG/cC/e8tZ3U0vqR/xU/whc08WMIKdPW19vYX8kMIQXJpt+kYfxN/3qDt9\nlIZmrK91yfOZv944PFZNXkIMJ6UCfpqzKkSU4bkCgYEA+nY4Lcfkt8HSkperDS5U\nzWQAMHlLiaQRT18V18HV5aNMzOAzwh/IaVZ8g0DRad2iYaVfDkYCEbbMs6O5Y3oY\n5rFfpcMg5XkU0h8r90RqE0GqBQy3CLVW47SoDwoP/rH6Mytrinxk4uzPtHnAYTI3\nwTd135KinJcNpuICeoheWHcCgYEAvvEhvCxqokcT1ZyZAaITY/LTzQ5SjIvCFjCz\nFDxCE5LHGpGxw9IZ+63RfuI0JPW0EBdQ10RoKVmK8y34Mwg4gdTVuEj5P3/3QX7N\n3FPd5JwIKZCUR8Jhqwhhe13780POS/XmUmo5zTjB8CxKtJ0IatQcQcqsYYzUUO3g\nwQkSirkCgYAUx0v/2E6MRCMxEC4bqNVWOM6fNuDiaV8aQ5wvSyBwrayIbq08lKBu\nxMMNrInzC3UWPr71Ey/GwnCXEqUlsJJySRLTUK3g+7uTdwyRtfZK5K6zPovMyCaO\nO4WZwc7z5VYJerewRIOmI9lTcqpYJe9kMzKvOp4M+acjSirEeZ3CHwKBgFdVw7Bm\nQH/pMtFJx1JP576Xmvj3zBos8qFjtQVUaoS5ZghpC34d43SSlHgMzvz4xVt2zqsn\nxtzi8AM6y4PMBsybpQWdmyPITDfQ4Cge1Cd0lucsEiagajvooW3kFxG1ue5Ukvyv\nSbDsfQh1udXS3b6/Ng2BvkcAOzypEVw54hlBAoGBALpZEfBg7hLk2Hs4o6iTz51E\nJFkbvI5EyfyYyS6PRpvjyGWrRGj/FuKp0xjZhCrzersx5251g92dXTzVSU82+kxA\nbG0TZVhRYTZZDn1XYjP3VHo2LvN20kyrg3XfsuBq//c+RIlQCN1epl9cHaOgO904\ny+tXRBTOBgtNO+eoX9WI\n-----END PRIVATE KEY-----\n","client_email"="gee-service-account@islas-calor-teapa.iam.gserviceaccount.com","client_id"="112420811139453325739","auth_uri"="https://accounts.google.com/o/oauth2/auth","token_uri"="https://oauth2.googleapis.com/token","auth_provider_x509_cert_url"="https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url"="https://www.googleapis.com/robot/v1/metadata/x509/gee-service-account%40islas-calor-teapa.iam.gserviceaccount.com","universe_domain"="googleapis.com"}
