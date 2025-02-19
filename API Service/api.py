from flask import Flask, request, jsonify
import psycopg2
import json

# """
# CREATE TABLE "signal_strength_prod" (
# 	"LATITUDE" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"LONGITUDE" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"LAC" INTEGER NOT NULL DEFAULT '0',
# 	"MCC" INTEGER NOT NULL DEFAULT '0',
# 	"MNC" INTEGER NOT NULL DEFAULT '0',
# 	"BST_LAT" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"BST_LON" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"SIGNAL_STRENGTH" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"NETWORK_TYPE" INTEGER NOT NULL DEFAULT '0',
# 	"OPERATOR_NAME" VARCHAR NOT NULL DEFAULT '0',
# 	"NETWORK_SPEED_UP" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"NETWORK_SPEED_DOWN" DOUBLE PRECISION(53) NOT NULL DEFAULT '0',
# 	"COUNTRY_CODE" INTEGER NOT NULL DEFAULT '0',
# 	"OPERATOR_CODE" INTEGER NOT NULL DEFAULT '0'
# )
# ;
# COMMENT ON COLUMN "signal_strength_prod"."LATITUDE" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."LONGITUDE" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."LAC" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."MCC" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."MNC" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."BST_LAT" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."BST_LON" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."SIGNAL_STRENGTH" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."NETWORK_TYPE" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."OPERATOR_NAME" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."NETWORK_SPEED_UP" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."NETWORK_SPEED_DOWN" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."COUNTRY_CODE" IS '';
# COMMENT ON COLUMN "signal_strength_prod"."OPERATOR_CODE" IS '';
# """
app = Flask(__name__)
con = psycopg2.connect(
    dbname="dd39gjupgu55bp",
    user="urbpnylcvchqhl",
    host="ec2-52-7-39-178.compute-1.amazonaws.com",
    password="ce93a69685e93e64fed547c6e901c15a88d14acfdfa40727141864d27afda991",
)


@app.route("/prod/add", methods=["POST"])
def add_ss_data():
    data = request.json
    # return data
    # return jsonify(
    #     {
    #         "LATITUDE": data["LATITUDE"],
    #         "LONGITUDE": data["LONGITUDE"],
    #         "LAC": data["LAC"],
    #         "MCC": data["MCC"],
    #         "MNC": data["MNC"],
    #         "BST_LAT": data["BST_LAT"],
    #         "BST_LON": data["BST_LON"],
    #         "SIGNAL_STRENGTH": data["SIGNAL_STRENGTH"],
    #         "NETWORK_TYPE": data["NETWORK_TYPE"],
    #         "OPERATOR_NAME": data["OPERATOR_NAME"],
    #         "NETWORK_SPEED_UP": data["NETWORK_SPEED_UP"],
    #         "NETWORK_SPEED_DOWN": data["NETWORK_SPEED_DOWN"],
    #         "COUNTRY_CODE": data["COUNTRY_CODE"],
    #         "OPERATOR_CODE": data["COUNTRY_CODE"],
    #     }
    # )
    cur = con.cursor()
    cur.execute(
        "INSERT INTO public.signal_strength_prod (latitude, longitude, lac, mcc, bst_lat, bst_lon, signal_strength, network_type, operator_name, network_speed_up, network_speed_down, country_code, operator_code, imei, wifi, mnc)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        [
            data["LATITUDE"],
            data["LONGITUDE"],
            data["LAC"],
            data["MCC"],
            data["BST_LAT"],
            data["BST_LON"],
            data["SIGNAL_STRENGTH"],
            data["NETWORK_TYPE"],
            data["OPERATOR_NAME"],
            data["NETWORK_SPEED_UP"],
            data["NETWORK_SPEED_DOWN"],
            data["COUNTRY_CODE"],
            data["OPERATOR_CODE"],
            data["IMEI"],
            data["WIFI"],
            data["MNC"],
        ],
    )
    con.commit()
    cur.close()
    return "ok"


@app.route("/prod/get", methods=["GET"])
def get_ss_data():
    cur = con.cursor()
    cur.execute("select * from signal_strength_prod")
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return jsonify(r)
    # return jsonify(cur.fetchall())

    # cur.execute(
    #     'INS ERT INTO signal_strength_prod("LATITUDE", "LONGITUDE", "LAC", "MCC", "MNC", "BST_LAT", "BST_LON", "SIGNAL_STRENGTH", "NETWORK_TYPE", "OPERATOR_NAME", "NETWORK_SPEED_UP", "NETWORK_SPEED_DOWN", "COUNTRY_CODE", "OPERATOR_CODE")VALUES(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)'
    # )
    # con.commit()
@app.route("/prod/get/jio", methods=["GET"])
def get_jio_data():
    cur = con.cursor()
    cur.execute("select * from signal_strength_prod where operator_name= 'JIO' OR operator_name= 'Jio 4G' ")
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return jsonify(r)

@app.route("/prod/get/airtel", methods=["GET"])
def get_airtel_data():
    cur = con.cursor()
    cur.execute("select * from signal_strength_prod where operator_name= 'airtel'")
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return jsonify(r)    

@app.route("/prod/get/vodafone", methods=["GET"])
def get_vodafone_data():
    cur = con.cursor()
    cur.execute("select * from signal_strength_prod where operator_name= 'vodafone'")
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return jsonify(r)

@app.route("/prod/get/bsnl", methods=["GET"])
def get_bsnl_data():
    cur = con.cursor()
    cur.execute("select * from signal_strength_prod where operator_name= 'bsnl'")
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    # cur.connection.close()
    return jsonify(r)

@app.route("/help", methods=["GET"])
def help():
    return jsonify(
        {
            "structure": {
                "LATITUDE": "DOUBLE",
                "LONGITUDE": "DOUBLE",
                "LAC": "INTEGER",
                "MCC": "INTEGER",
                "MNC": "INTEGER",
                "BST_LAT": "DOUBLE",
                "BST_LON": "DOUBLE",
                "SIGNAL_STRENGTH": "DOUBLE",
                "NETWORK_TYPE": "INTEGER",
                "OPERATOR_NAME": "VARCHAR",
                "NETWORK_SPEED_UP": "DOUBLE",
                "NETWORK_SPEED_DOWN": "DOUBLE",
                "COUNTRY_CODE": "INTEGER",
                "OPERATOR_CODE": "INTEGER",
            },
            "format": {
                "LATITUDE": 'data["LATITUDE"]',
                "LONGITUDE": 'data["LONGITUDE"]',
                "LAC": 'data["LAC"]',
                "MCC": 'data["MCC"]',
                "MNC": 'data["MNC"]',
                "BST_LAT": 'data["BST_LAT"]',
                "BST_LON": 'data["BST_LON"]',
                "SIGNAL_STRENGTH": 'data["SIGNAL_STRENGTH"]',
                "NETWORK_TYPE": 'data["NETWORK_TYPE"]',
                "OPERATOR_NAME": 'data["OPERATOR_NAME"]',
                "NETWORK_SPEED_UP": 'data["NETWORK_SPEED_UP"]',
                "NETWORK_SPEED_DOWN": 'data["NETWORK_SPEED_DOWN"]',
                "COUNTRY_CODE": 'data["COUNTRY_CODE"]',
                "OPERATOR_CODE": 'data["COUNTRY_CODE"]',
            },
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
