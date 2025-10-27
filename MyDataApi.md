股票列表
API接口：http://api.mairuiapi.com/hslt/list/您的licence
演示URL：http://api.mairuiapi.com/hslt/list/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：获取基础的股票代码和名称，用于后续接口的参数传入。
数据更新：每日16:20
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	股票代码，如：000001
mc	string	股票名称，如：平安银行
jys	string	交易所，"sh"表示上证，"sz"表示深证

新股日历
API接口：http://api.mairuiapi.com/hslt/new/您的licence
演示URL：http://api.mairuiapi.com/hslt/new/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：新股日历，按申购日期倒序。
数据更新：每日17:00
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
zqdm	string	股票代码
zqjc	string	股票简称
sgdm	string	申购代码
fxsl	number	发行总数（股）
swfxsl	number	网上发行（股）
sgsx	number	申购上限（股）
dgsz	number	顶格申购需配市值(元)
sgrq	string	申购日期
fxjg	number	发行价格（元），null为“未知”
zxj	number	最新价（元），null为“未知”
srspj	number	首日收盘价（元），null为“未知”
zqgbrq	string	中签号公布日，null为未知
zqjkrq	string	中签缴款日，null为未知
ssrq	string	上市日期，null为未知
syl	number	发行市盈率，null为“未知”
hysyl	number	行业市盈率
wszql	number	中签率（%），null为“未知”
yzbsl	number	连续一字板数量，null为“未知”
zf	number	涨幅（%），null为“未知”
yqhl	number	每中一签获利（元），null为“未知”
zyyw	string	主营业务

指数、行业、概念树
API接口：http://api.mairuiapi.com/hszg/list/您的licence
演示URL：http://api.mairuiapi.com/hszg/list/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：获取指数、行业、概念（包括基金，债券，美股，外汇，期货，黄金等的代码），其中isleaf为1（叶子节点）的记录的code（代码）可以作为下方接口的参数传入，从而得到某个指数、行业、概念下的相关股票。
数据更新：每周六03:05
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
name	string	名称
code	string	代码
type1	number	一级分类（0:A股,1:创业板,2:科创板,3:基金,4:香港股市,5:债券,6:美国股市,7:外汇,8:期货,9:黄金,10:英国股市）
type2	number	二级分类（0:A股-申万行业,1:A股-申万二级,2:A股-热门概念,3:A股-概念板块,4:A股-地域板块,5:A股-证监会行业,6:A股-分类,7:A股-指数成分,8:A股-风险警示,9:A股-大盘指数,10:A股-次新股,11:A股-沪港通,12:A股-深港通,13:基金-封闭式基金,14:基金-开放式基金,15:基金-货币型基金,16:基金-ETF基金净值,17:基金-ETF基金行情,18:基金-LOF基金行情,21:基金-科创板基金,22:香港股市-恒生行业,23:香港股市-全部港股,24:香港股市-热门港股,25:香港股市-蓝筹股,26:香港股市-红筹股,27:香港股市-国企股,28:香港股市-创业板,29:香港股市-指数,30:香港股市-A+H,31:香港股市-窝轮,32:香港股市-ADR,33:香港股市-沪港通,34:香港股市-深港通,35:香港股市-中华系列指数,36:债券-沪深债券,37:债券-深市债券,38:债券-沪市债券,39:债券-沪深可转债,40:美国股市-中国概念股,41:美国股市-科技类,42:美国股市-金融类,43:美国股市-制造零售类,44:美国股市-汽车能源类,45:美国股市-媒体类,46:美国股市-医药食品类,48:外汇-基本汇率,49:外汇-热门汇率,50:外汇-所有汇率,51:外汇-交叉盘汇率,52:外汇-美元相关汇率,53:外汇-人民币相关汇率,54:期货-全球期货,55:期货-中国金融期货交易所,56:期货-上海期货交易所,57:期货-大连商品交易所,58:期货-郑州商品交易所,59:黄金-黄金现货,60:黄金-

黄金期货
level	number	层级，从0开始，根节点为0，二级节点为1，以此类推
pcode	string	父节点代码
pname	string	父节点名称
isleaf	number	是否为叶子节点，0：否，1：是

根据指数、行业、概念找相关股票
API接口：http://api.mairuiapi.com/hszg/gg/指数、行业、概念代码/您的licence
演示URL：http://api.mairuiapi.com/hszg/gg/sw_sysh/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据“指数、行业、概念树”接口得到的代码作为参数，得到相关的股票。
数据更新：每周六11:00
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	代码（根据接口参数可能是A股股票代码，也可能是其他指数、行业、概念的股票代码）
mc	string	名称（根据接口参数可能是A股股票代码，也可能是其他指数、行业、概念的股票名称）
jys	string	交易所，"sh"表示上证，"sz"表示深证（如果返回的是A股的股票，那么有值，否则是null）

根据股票找相关指数、行业、概念
API接口：http://api.mairuiapi.com/hszg/zg/股票代码(如000001)/您的licence
演示URL：http://api.mairuiapi.com/hszg/zg/000001/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码作为参数，得到相关的指数、行业、概念。
数据更新：每周六11:00
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
code	string	指数、行业、概念代码，如：sw2_650300
name	string	指数、行业、概念名称，如：沪深股市-申万二级-国防军工-地面兵装

涨停股池
API接口：http://api.mairuiapi.com/hslt/ztgc/日期(如2020-01-15)/您的licence
演示URL：http://api.mairuiapi.com/hslt/ztgc/2024-01-10/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据日期（格式yyyy-MM-dd，从2019-11-28开始到现在的每个交易日）作为参数，得到每天的涨停股票列表，根据封板时间升序。
数据更新：交易时间段每10分钟
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	代码
mc	string	名称
p	number	价格（元）
zf	number	涨幅（%）
cje	number	成交额（元）
lt	number	流通市值（元）
zsz	number	总市值（元）
hs	number	换手率（%）
lbc	number	连板数
fbt	string	首次封板时间（HH:mm:ss）
lbt	string	最后封板时间（HH:mm:ss）
zj	number	封板资金（元）
zbc	number	炸板次数
tj	string	涨停统计（x天/y板）
hy	string	所属行业
hy	string	所属行业
hy	string	所属行业
hy	string	所属行业
hy	string	所属行业
hy	string	所属行业

跌停股池
API接口：http://api.mairuiapi.com/hslt/dtgc/日期(如2020-01-15)/您的licence
演示URL：http://api.mairuiapi.com/hslt/dtgc/2024-01-10/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据日期（格式yyyy-MM-dd，从2019-11-28开始到现在的每个交易日）作为参数，得到每天的跌停股票列表，根据封单资金升序。
数据更新：交易时间段每10分钟
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	代码
mc	string	名称
p	number	价格（元）
zf	number	跌幅（%）
cje	number	成交额（元）
lt	number	流通市值（元）
zsz	number	总市值（元）
pe	number	动态市盈率
hs	number	换手率（%）
lbc	number	连续跌停次数
lbt	string	最后封板时间（HH:mm:ss）
zj	number	封单资金（元）
fba	number	板上成交额（元）
zbc	number	开板次数

强势股池
API接口：http://api.mairuiapi.com/hslt/qsgc/日期(如2020-01-15)/您的licence
演示URL：http://api.mairuiapi.com/hslt/qsgc/2024-01-10/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据日期（格式yyyy-MM-dd，从2019-11-28开始到现在的每个交易日）作为参数，得到每天的强势股票列表，根据涨幅倒序。
数据更新：交易时间段每10分钟
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	代码
mc	string	名称
p	number	价格（元）
ztp	number	涨停价（元）
zf	number	涨幅（%）
cje	number	成交额（元）
lt	number	流通市值（元）
zsz	number	总市值（元）
zs	number	涨速（%）
nh	number	是否新高（0：否，1：是）
lb	number	量比
hs	number	换手率（%）
tj	string	涨停统计（x天/y板）

次新股池
API接口：http://api.mairuiapi.com/hslt/cxgc/日期(如2020-01-15)/您的licence
演示URL：http://api.mairuiapi.com/hslt/cxgc/2024-01-10/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据日期（格式yyyy-MM-dd，从2019-11-28开始到现在的每个交易日）作为参数，得到每天的次新股票列表，根据开板几日升序。
数据更新：交易时间段每10分钟
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	代码
mc	string	名称
p	number	价格（元）
ztp	number	涨停价（元，无涨停价为null）
zf	number	涨跌幅（%）
cje	number	成交额（元）
lt	number	流通市值（元）
zsz	number	总市值（元）
nh	number	是否新高（0：否，1：是）
hs	number	转手率（%）
tj	string	涨停统计（x天/y板）
kb	number	开板几日
od	string	开板日期（yyyyMMdd）
ipod	string	上市日期（yyyyMMdd）

炸板股池
API接口：http://api.mairuiapi.com/hslt/zbgc/日期(如2020-01-15)/您的licence
演示URL：http://api.mairuiapi.com/hslt/zbgc/2024-01-10/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据日期（格式yyyy-MM-dd，从2019-11-28开始到现在的每个交易日）作为参数，得到每天的炸板股票列表，根据首次封板时间升序。
数据更新：交易时间段每10分钟
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	代码
mc	string	名称
p	number	价格（元）
ztp	number	涨停价（元）
zf	number	涨跌幅（%）
cje	number	成交额（元）
lt	number	流通市值（元）
zsz	number	总市值（元）
zs	number	涨速（%）
hs	number	转手率（%）
tj	string	涨停统计（x天/y板）
fbt	string	首次封板时间（HH:mm:ss）
zbc	number	炸板次数

实时交易数据（网络数据源）
API接口：http://api.mairuiapi.com/hsrl/ssjy/股票代码(如000001)/您的licence
演示URL：http://api.mairuiapi.com/hsrl/ssjy/000001/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码获取实时交易数据（您可以理解为日线的最新数据），该接口为网络公开数据源，非券商数据源。
数据更新：交易时间段每1分钟
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
fm	number	五分钟涨跌幅（%）
h	number	最高价（元）
hs	number	换手（%）
lb	number	量比（%）
l	number	最低价（元）
lt	number	流通市值（元）
o	number	开盘价（元）
pe	number	市盈率（动态，总市值除以预估全年净利润，例如当前公布一季度净利润1000万，则预估全年净利润4000万）
pc	number	涨跌幅（%）
p	number	当前价格（元）
sz	number	总市值（元）
cje	number	成交额（元）
ud	number	涨跌额（元）
v	number	成交量（手）
yc	number	昨日收盘价（元）
zf	number	振幅（%）
zs	number	涨速（%）
sjl	number	市净率
zdf60	number	60日涨跌幅（%）
zdfnc	number	年初至今涨跌幅（%）
t	string	更新时间yyyy-MM-ddHH:mm:ss

当天逐笔交易
API接口：http://api.mairuiapi.com/hsrl/zbjy/股票代码(如000001)/您的licence
演示URL：http://api.mairuiapi.com/hsrl/zbjy/000001/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码获取当天逐笔交易数据，按时间倒序。
数据更新：每日21:00
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
d	string	数据归属日期（yyyy-MM-dd）
t	string	时间（HH:mm:dd）
v	number	成交量（股）
p	number	成交价
ts	number	交易方向（0：中性盘，1：买入，2：卖出）

实时交易数据（券商数据源）
API接口：http://api.mairuiapi.com/hsstock/real/time/股票代码/证书您的licence
演示URL：http://api.mairuiapi.com/hsstock/real/time/000001/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码获取实时交易数据（您可以理解为日线的最新数据）。
数据更新：实时
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
p	number	最新价
o	number	开盘价
h	number	最高价
l	number	最低价
yc	number	前收盘价
cje	number	成交总额
v	number	成交总量
pv	number	原始成交总量
ud	float	涨跌额
pc	float	涨跌幅
zf	float	振幅
t	string	更新时间
pe	number	市盈率
tr	number	换手率
pb_ratio	number	市净率
tv	number	成交量

买卖五档盘口
API接口：http://api.mairuiapi.com/hsstock/real/five/股票代码/证书您的licence
演示URL：http://api.mairuiapi.com/hsstock/real/five/000001/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码获取实时买卖五档盘口数据。
数据更新：实时
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
ps	number	委卖价
pb	number	委买价
vs	number	委卖量
vb	number	委买量
t	string	更新时间

实时交易数据（全部 | 券商数据源）
API接口：http://a.mairuiapi.com/hsrl/ssjy/all/您的licence
演示URL：http://a.mairuiapi.com/hsrl/ssjy/all/您的licence
接口说明：一次性获取《股票列表》中所有股票的实时交易数据（您可以理解为日线的最新数据），该接口仅限钻石版和包年版证书使用且限制每分钟请求1次。
数据更新：实时
请求频率：1分钟1次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
dm	string	股票代码
p	number	最新价
o	number	开盘价
h	number	最高价
l	number	最低价
yc	number	前收盘价
cje	number	成交总额
v	number	成交总量
pv	number	原始成交总量
ud	float	涨跌额
pc	float	涨跌幅
zf	float	振幅
t	string	更新时间
pe	number	市盈率
tr	number	换手率
pb_ratio	number	市净率
tv	number	成交量

实时交易数据（多股）
API接口：http://api.mairuiapi.com/hsrl/ssjy_more/您的licence?stock_codes=股票代码1,股票代码2……股票代码20
演示URL：http://api.mairuiapi.com/hsrl/ssjy_more/LICENCE-66D8-9F96-0C7F0FBCD073?stock_codes=000001,000002,000004
接口说明：一次性获取《股票列表》中不超过20支股票的实时交易数据（您可以理解为日线的最新数据）
数据更新：实时
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
p	number	最新价
o	number	开盘价
h	number	最高价
l	number	最低价
yc	number	前收盘价
cje	number	成交总额
v	number	成交总量
pv	number	原始成交总量
ud	float	涨跌额
pc	float	涨跌幅
zf	float	振幅
t	string	更新时间
pe	number	市盈率
tr	number	换手率
pb_ratio	number	市净率
tv	number	成交量

实时交易数据（全部 | 网络数据源）
API接口：http://a.mairuiapi.com/hsrl/real/all/您的licence
演示URL：http://a.mairuiapi.com/hsrl/ssjy/all/您的licence
接口说明：一次性获取《股票列表》中所有股票的实时交易数据（您可以理解为日线的最新数据），该接口仅限钻石版和包年版证书使用且限制每分钟请求1次。
数据更新：交易时间段每1分钟
请求频率：1分钟1次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
fm	number	五分钟涨跌幅（%）
h	number	最高价（元）
hs	number	换手（%）
lb	number	量比（%）
l	number	最低价（元）
lt	number	流通市值（元）
o	number	开盘价（元）
pe	number	市盈率（动态，总市值除以预估全年净利润，例如当前公布一季度净利润1000万，则预估全年净利润4000万）
pc	number	涨跌幅（%）
p	number	当前价格（元）
sz	number	总市值（元）
cje	number	成交额（元）
ud	number	涨跌额（元）
v	number	成交量（手）
yc	number	昨日收盘价（元）
zf	number	振幅（%）
zs	number	涨速（%）
sjl	number	市净率
zdf60	number	60日涨跌幅（%）
zdfnc	number	年初至今涨跌幅（%）
t	string	更新时间yyyy-MM-ddHH:mm:ss

资金流向数据
API接口：http://api.mairuiapi.com/hsstock/history/transaction/股票代码(如000001)/您的licence?st=开始时间&et=结束时间&lt=最新条数
演示URL：http://api.mairuiapi.com/hsstock/history/transaction/000001/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码获取资金流向数据。开始时间以及结束时间的格式均为 YYYYMMDD，例如：'20240101'，不设置开始时间和结束时间则为全部历史数据。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。下列字段中，特大单为成交金额大于或等于100万元或成交量大于或等于5000手，大单为成交金额大于或等于20万元或成交量大于或等于1000手，中单为成交金额大于或等于4万元或成交量大于或等于200手，其他为小单。
数据更新：每日21:30更新
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	int	交易时间
zmbzds	int	主买单总单数
zmszds	int	主卖单总单数
dddx	float	大单动向
zddy	float	涨跌动因
ddcf	float	大单差分
zmbzdszl	int	主买单总单数增量
zmszdszl	int	主卖单总单数增量
cjbszl	int	成交笔数增量
zmbtdcje	float	主买特大单成交额
zmbddcje	float	主买大单成交额
zmbzdcje	float	主买中单成交额
zmbxdcje	float	主买小单成交额
zmbljcje	float	主买累计成交额
zmstdcje	float	主卖特大单成交额
zmsddcje	float	主卖大单成交额
zmszdcje	float	主卖中单成交额
zmsxdcje	float	主卖小单成交额
zmsljcje	float	主卖累计成交额
bdmbtdcje	float	被动买特大单成交额
bdmbddcje	float	被动买大单成交额
bdmbzdcje	float	被动买中单成交额
bdmbxdcje	float	被动买小单成交额
bdmbljcje	float	被动买累计成交额
bdmstdcje	float	被动卖特大单成交额
bdmsddcje	float	被动卖大单成交额
bdmszdcje	float	被动卖中单成交额
bdmsxdcje	float	被动卖小单成交额
bdmsljcje	float	被动卖累计成交额
jlrcdcje	float	净流入超大单成交额
jlrddcje	float	净流入大单成交额
jlrzdcje	float	净流入中单成交额
jlrxdcje	float	净流入小单成交额
zmbtdcjl	int	主买特大单成交量
zmbddcjl	int	主买大单成交量
zmbzdcjl	int	主买中单成交量
zmbxdcjl	int	主买小单成交量
zmbljcjl	int	主买累计成交量
zmstdcjl	int	主卖特大单成交量
zmsddcjl	int	主卖大单成交量
zmszdcjl	int	主卖中单成交量
zmsxdcjl	int	主卖小单成交量
zmsljcjl	int	主卖累计成交量
bdmbtdcjl	int	被动买特大单成交量
bdmbddcjl	int	被动买大单成交量
bdmbzdcjl	int	被动买中单成交量
bdmbxdcjl	int	被动买小单成交量
bdmbljcjl	int	被动买累计成交量
bdmstdcjl	int	被动卖特大单成交量
bdmsddcjl	int	被动卖大单成交量
bdmszdcjl	int	被动卖中单成交量
bdmsxdcjl	int	被动卖小单成交量
bdmsljcjl	int	被动卖累计成交量
jlrcdcjl	int	净流入超大单成交量
jlrddcjl	int	净流入大单成交量
jlrzdcjl	int	净流入中单成交量
jlrxdcjl	int	净流入小单成交量
zmbtdcjzl	float	主买特大单成交额增量
zmbddcjzl	float	主买大单成交额增量
zmbzdcjzl	float	主买中单成交额增量
zmbxdcjzl	float	主买小单成交额增量
zmbljcjzl	float	主买累计成交额增量
zmstdcjzl	float	主卖特大单成交额增量
zmsddcjzl	float	主卖大单成交额增量
zmszdcjzl	float	主卖中单成交额增量
zmsxdcjzl	float	主卖小单成交额增量
zmsljcjzl	float	主卖累计成交额增量
bdmbtdcjzl	float	被动买特大单成交额增量
bdmbddcjzl	float	被动买大单成交额增量
bdmbzdcjzl	float	被动买中单成交额增量
bdmbxdcjzl	float	被动买小单成交额增量
bdmbljcjzl	float	被动买累计成交额增量
bdmstdcjzl	float	被动卖特大单成交额增量
bdmsddcjzl	float	被动卖大单成交额增量
bdmszdcjzl	float	被动卖中单成交额增量
bdmsxdcjzl	float	被动卖小单成交额增量
bdmsljcjzl	float	被动卖累计成交额增量
jlrcdcjzl	float	净流入超大单成交额增量
jlrddcjzl	float	净流入大单成交额增量
jlrzdcjzl	float	净流入中单成交额增量
jlrxdcjzl	float	净流入小单成交额增量
zmbtdcjzlv	int	主买特大单成交量增量
zmbddcjzlv	int	主买大单成交量增量
zmbzdcjzlv	int	主买中单成交量增量
zmbxdcjzlv	int	主买小单成交量增量
zmbljcjzlv	int	主买累计成交量增量
zmstdcjzlv	int	主卖特大单成交量增量
zmsddcjzlv	int	主卖大单成交量增量
zmszdcjzlv	int	主卖中单成交量增量
zmsxdcjzlv	int	主卖小单成交量增量
zmsljcjzlv	int	主卖累计成交量增量
bdmbtdcjzlv	int	被动买特大单成交量增量
bdmbddcjzlv	int	被动买大单成交量增量
bdmbzdcjzlv	int	被动买中单成交量增量
bdmbxdcjzlv	int	被动买小单成交量增量
bdmbljcjzlv	int	被动买累计成交量增量
bdmstdcjzlv	int	被动卖特大单成交量增量
bdmsddcjzlv	int	被动卖大单成交量增量
bdmszdcjzlv	int	被动卖中单成交量增量
bdmsxdcjzlv	int	被动卖小单成交量增量

最新分时交易
API接口：http://api.mairuiapi.com/hsstock/latest/股票代码.市场（如000001.SZ）/分时级别(如d)/除权方式/您的licence?lt=最新条数(如5)
演示URL：https://api.mairuiapi.com/hsstock/latest/000001.SZ/d/n/LICENCE-66D8-9F96-0C7F0FBCD073?lt=1
接口说明：根据《股票列表》得到的股票代码和分时级别获取最新交易数据，交易时间升序。目前分时级别支持5分钟、15分钟、30分钟、60分钟、日线、周线、月线、年线，对应的请求参数分别为5、15、30、60、d、w、m、y，日线以上除权方式有不复权、前复权、后复权、等比前复权、等比后复权，对应的参数分别为n、f、b、fr、br，分钟级无除权数据，对应的参数为n。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。
数据更新：实时
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易时间
o	float	开盘价
h	float	最高价
l	float	最低价
c	float	收盘价
v	float	成交量
a	float	成交额
pc	float	前收盘价
sf	int	停牌 1停牌，0 不停牌

历史分时交易
API接口：http://api.mairuiapi.com/hsstock/history/股票代码.市场（如000001.SZ）/分时级别(如d)/除权方式/您的licence?st=开始时间(如20240601)&et=结束时间(如20250430)&lt=最新条数(如100)
演示URL：https://api.mairuiapi.com/hsstock/history/000001.SZ/d/n/LICENCE-66D8-9F96-0C7F0FBCD073?st=20250101&et=20250430&lt=100
接口说明：根据《股票列表》得到的股票代码和分时级别获取历史交易数据，交易时间升序。目前分时级别支持5分钟、15分钟、30分钟、60分钟、日线、周线、月线、年线，对应的请求参数分别为5、15、30、60、d、w、m、y，日线以上除权方式有不复权、前复权、后复权、等比前复权、等比后复权，对应的参数分别为n、f、b、fr、br，分钟级无除权数据，对应的参数为n。开始时间以及结束时间的格式均为 YYYYMMDD 或 YYYYMMDDhhmmss，例如：'20240101' 或'20241231235959'。不设置开始时间和结束时间则为全部历史数据。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。
数据更新：分钟级别数据盘中更新，分时越小越优先更新，如5分钟级别会每5分钟更新，15分钟级别会每15分钟更新，以此类推，日线及以上级别每日15:30开始更新，预计17:10完成
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易时间
o	float	开盘价
h	float	最高价
l	float	最低价
c	float	收盘价
v	float	成交量
a	float	成交额
pc	float	前收盘价
sf	int	停牌 1停牌，0 不停牌

历史涨跌停价格
API接口：http://api.mairuiapi.com/hsstock/stopprice/history/股票代码（如000001.SZ）/您的licence?st=开始时间&et=结束时间
演示URL：http://api.mairuiapi.com/hsstock/stopprice/history/000001.SZ/LICENCE-66D8-9F96-0C7F0FBCD073?st=20240501&et=20240601
接口说明：根据《股票列表》得到的股票代码获取历史涨跌停价格，开始时间以及结束时间的格式均为 YYYYMMDD，例如：'20240101'。不设置开始时间和结束时间则为全部历史数据。
数据更新：每日0点
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易日期
h	float	涨停价格
l	float	跌停价格

行情指标
API接口：http://api.mairuiapi.com/hsstock/indicators/股票代码（如000001.SZ）/您的licence?st=开始时间&et=结束时间
演示URL：http://api.mairuiapi.com/hsstock/indicators/600519.SH/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码获取各项行情指标，开始时间以及结束时间的格式均为 YYYYMMDD，例如：'20240101'。不设置开始时间和结束时间则为全部数据。
数据更新：每日下午16:30开始更新，预计20:00完成更新
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
time	string	更新时间
lb	float	量比
om	float	1分钟涨速(%)
fm	float	5分钟涨速(%)
3d	float	3日涨幅(%)
5d	float	5日涨幅(%)
10d	float	10日涨幅(%)
3t	float	3日换手(%)
5t	float	5日换手(%)
10t	float	10日换手(%)

历史分时MACD
API接口：http://api.mairuiapi.com/hsstock/history/macd/股票代码(如000001.SZ)/分时级别(如d)/除权类型(如n)/您的licence?st=开始时间&et=结束时间&lt=最新条数
演示URL：http://api.mairuiapi.com/hsstock/history/macd/000001.SZ/d/n/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码和分时级别获取历史MACD数据，交易时间升序。目前分时级别支持5分钟、15分钟、30分钟、60分钟、日线、周线、月线、年线，对应的请求参数分别为5、15、30、60、d、w、m、y，日线以上除权方式有不复权、前复权、后复权、等比前复权、等比后复权，对应的参数分别为n、f、b、fr、br，分钟级仅限请求不复权数据，对应的参数为n。开始时间以及结束时间的格式均为 YYYYMMDD 或 YYYYMMDDhhmmss，例如：'20240101' 或'20241231235959'。不设置开始时间和结束时间则为全部历史数据。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。
数据更新：分钟级别数据盘中更新，分时越小越优先更新，如5分钟级别会每5分钟更新，15分钟级别会每15分钟更新，以此类推，日线及以上级别每日15:35更新
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易时间，短分时级别格式为yyyy-MM-ddHH:mm:ss，日线级别为yyyy-MM-dd
diff	number	DIFF值
dea	number	DEA值
macd	number	MACD值
ema12	number	EMA（12）值
ema26	number	EMA（26）值

历史分时MA
API接口：http://api.mairuiapi.com/hsstock/history/ma/股票代码(如000001.SZ)/分时级别(如d)/除权类型(如n)/您的licence?st=开始时间&et=结束时间&lt=最新条数
演示URL：http://api.mairuiapi.com/hsstock/history/ma/000001.SZ/d/n/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码和分时级别获取历史MA数据，交易时间升序。目前分时级别支持5分钟、15分钟、30分钟、60分钟、日线、周线、月线、年线，对应的请求参数分别为5、15、30、60、d、w、m、y，日线以上除权方式有不复权、前复权、后复权、等比前复权、等比后复权，对应的参数分别为n、f、b、fr、br，分钟级仅限请求不复权数据，对应的参数为n。开始时间以及结束时间的格式均为 YYYYMMDD 或 YYYYMMDDhhmmss，例如：'20240101' 或'20241231235959'。不设置开始时间和结束时间则为全部历史数据。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。
数据更新：分钟级别数据盘中更新，分时越小越优先更新，如5分钟级别会每5分钟更新，15分钟级别会每15分钟更新，以此类推，日线及以上级别每日15:35更新
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易时间，短分时级别格式为yyyy-MM-ddHH:mm:ss，日线级别为yyyy-MM-dd
ma3	number	MA3，没有则为null
ma5	number	MA5，没有则为null
ma10	number	MA10，没有则为null
ma15	number	MA15，没有则为null
ma20	number	MA20，没有则为null
ma30	number	MA30，没有则为null
ma60	number	MA60，没有则为null
ma120	number	MA120，没有则为null
ma200	number	MA200，没有则为null
ma250	number	MA250，没有则为null

历史分时BOLL
API接口：http://api.mairuiapi.com/hsstock/history/boll/股票代码(如000001.SZ)/分时级别(如d)/除权类型(如n)/您的licence?st=开始时间&et=结束时间&lt=最新条数
演示URL：http://api.mairuiapi.com/hsstock/history/boll/000001.SZ/d/n/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码和分时级别获取历史BOLL数据，交易时间升序。目前分时级别支持5分钟、15分钟、30分钟、60分钟、日线、周线、月线、年线，对应的请求参数分别为5、15、30、60、d、w、m、y，日线以上除权方式有不复权、前复权、后复权、等比前复权、等比后复权，对应的参数分别为n、f、b、fr、br，分钟级仅限请求不复权数据，对应的参数为n。开始时间以及结束时间的格式均为 YYYYMMDD 或 YYYYMMDDhhmmss，例如：'20240101' 或'20241231235959'。不设置开始时间和结束时间则为全部历史数据。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。
数据更新：分钟级别数据盘中更新，分时越小越优先更新，如5分钟级别会每5分钟更新，15分钟级别会每15分钟更新，以此类推，日线及以上级别每日15:35更新
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易时间，短分时级别格式为yyyy-MM-ddHH:mm:ss，日线级别为yyyy-MM-dd
u	number	上轨
d	number	下轨
m	number	中轨

历史分时KDJ
API接口：http://api.mairuiapi.com/hsstock/history/kdj/股票代码(如000001.SZ)/分时级别(如d)/除权类型(如n)/您的licence?st=开始时间&et=结束时间&lt=最新条数
演示URL：http://api.mairuiapi.com/hsstock/history/kdj/000001.SZ/d/n/LICENCE-66D8-9F96-0C7F0FBCD073
接口说明：根据《股票列表》得到的股票代码和分时级别获取历史KDJ数据，交易时间升序。目前分时级别支持5分钟、15分钟、30分钟、60分钟、日线、周线、月线、年线，对应的请求参数分别为5、15、30、60、d、w、m、y，日线以上除权方式有不复权、前复权、后复权、等比前复权、等比后复权，对应的参数分别为n、f、b、fr、br，分钟级仅限请求不复权数据，对应的参数为n。开始时间以及结束时间的格式均为 YYYYMMDD 或 YYYYMMDDhhmmss，例如：'20240101' 或'20241231235959'。不设置开始时间和结束时间则为全部历史数据。同时可以指定获取数据条数，例如指定lt=10，则获取最新的10条数据。
数据更新：分钟级别数据盘中更新，分时越小越优先更新，如5分钟级别会每5分钟更新，15分钟级别会每15分钟更新，以此类推，日线及以上级别每日15:35更新
请求频率：1分钟300次 | 包年版1分钟3千次 | 钻石版1分钟6千次
返回格式：标准Json格式      [{},...{}]
字段名称	数据类型	字段说明
t	string	交易时间，短分时级别格式为yyyy-MM-ddHH:mm:ss，日线级别为yyyy-MM-dd
k	number	K值
d	number	D值
j	number	J值