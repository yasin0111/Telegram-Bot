from config import LANG

# Response Messages Template
MESSAGES = {
    'EN': {
        'WELCOME': 'Welcome to users bot',
        'INFO_USER': '📄Your Subscription Info',
        'SUBSCRIPTION_STATUS': '☑️Status:',
        'ACTIVE_SUBSCRIPTION_STATUS': '🟢 Active',
        'DEACTIVE_SUBSCRIPTION_STATUS': '🔴 Deactive',
        'INFO_USAGE': '📊Usage:',
        'INFO_REMAINING_DAYS': '⏳Remaining Days:',
        'INFO_ID': '🔑UUID:',
        'OF': 'of',
        'GB': 'GB',
        'DAY_EXPIRE': 'Days',
        'CONFIRM_SUBSCRIPTION_QUESTION': 'Is this your subscription?',
        'NAME': 'Name:',
        'CANCEL_SUBSCRIPTION': 'Subscription not confirmed',
        'SUBSCRIPTION_CONFIRMED': 'Your subscription has been confirmed. Now you can get your subscription status.',
        'WAIT': 'Please wait...',
        'UNKNOWN_ERROR': 'Unknown error!',
        'ENTER_SUBSCRIPTION_INFO': 'Please enter your subscription info\n One of the configs, uuid or subscription link',
        'SUBSCRIPTION_INFO_NOT_FOUND': 'Subscription info not found!',
        'SUBSCRIPTION_UNLINKED': 'Subscription unlinked!',
        'USER_NOT_FOUND': 'User not found!',
        'USER_NAME': '👤Name:',
        'PLANS_LIST': '📋Plans List:',
        'PLANS_NOT_FOUND': 'Plans not found!',
        'PLAN_ADD_NAME': 'Please enter your name:',
        'SUBSCRIPTION_SUCCESS_ADDED': 'Your subscription has been successfully added.',
        'PLAN_INFO': '📄Plan Info:',
        'PLAN_INFO_SIZE': 'Size:',
        'PLAN_INFO_DAYS': 'Days:',
        'PLAN_INFO_PRICE': 'Price:',
        'TOMAN': 'T',
        'REQUEST_SEND_SCREENSHOT': 'Please send your payment receipt.',
        'ERROR_TYPE_SEND_SCREENSHOT': 'Please send your payment receipt as a photo!',
        'REQUEST_SEND_NAME': 'Please send your name.',
        'NO_SUBSCRIPTION': 'You have no subscription!',
        'WAIT_FOR_ADMIN_CONFIRMATION': '✅Your subscription is waiting for confirmation by the admin.\nPlease wait...',
        'NEW_PAYMENT_RECEIVED': 'New payment received',
        'PAYMENT_ASK_TO_CONFIRM': 'Do you want to confirm this payment?',
        'REQUEST_SEND_TO_QR': 'Please send your config or subscription link:',
        'REQUEST_SEND_TO_QR_ERROR': 'Please send your config or subscription!',
        'USER_CONFIGS_LIST': '📋Your Configs:',
        'USER_CONFIGS_NOT_FOUND': 'Configs not found!',
        'ERROR_CONFIG_NOT_FOUND': 'Config not found!',
        'ERROR_INVALID_COMMAND': 'Invalid command!',
        'ALREADY_SUBSCRIBED': 'You are already subscribed!',
        'ERROR_INVALID_NUMBER': 'Invalid number!',
        'CANCELED': 'Cancelled!',
        'SUBSCRIPTION_NOT_FOUND': 'Subscription not found!',
        'ZERO_BALANCE': '🔻Your wallet balance is zero',
        'WALLET_INFO_PART_1': '🔻Your wallet balance is',
        'WALLET_INFO_PART_2': '',
        'INCREASE_WALLET_BALANCE_AMOUNT': '🔻Please enter the amount that you want to charge your wallet in Tomans',
        'MINIMUM_DEPOSIT_AMOUNT':'🔻Please enter an amount greater than 30000 Tomans',
        'LACK_OF_WALLET_BALANCE':'❌Your wallet balance is not enough\nplease top up your wallet',
        'ORDER_ID': 'Order number:',
        'PAYMENT_CONFIRMED': '✅Payment confirmed',
        'ALREADY_RECEIVED_FREE': 'You have already received your free test account!',
        'GET_FREE_CONFIRMED' :  '✅Your free account has been successfully registered',
        'SUCCESSFUL_RENEWAL': '✅Your subscription has been successfully renewed',
        'REQUEST_START': 'Please update the bot with /start command',
    },
    'FA': {
        'WELCOME': "به ربات کاربران خوش آمدید",
        'INFO_USER': '📄اطلاعات اشتراک شما',
        'SUBSCRIPTION_STATUS': '❔وضعیت:',
        'ACTIVE_SUBSCRIPTION_STATUS': '🟢 فعال',
        'DEACTIVE_SUBSCRIPTION_STATUS': '🔴 غیر فعال',
        'INFO_USAGE': '📊میزان استفاده:',
        'INFO_REMAINING_DAYS': '⏳زمان باقی مانده:',
        'INFO_ID': '🔑شناسه:',
        'OF': 'از',
        'GB': 'گیگ',
        'DAY_EXPIRE': 'روز',
        'CONFIRM_SUBSCRIPTION_QUESTION': 'آیا این اشتراک شماست؟',
        'NAME': 'نام:',
        'CANCEL_SUBSCRIPTION': '❌اشتراک تایید نشد',
        'SUBSCRIPTION_CONFIRMED': '✅اشتراک شما تایید شد. حالا میتوانید وضعیت اشتراک خود را دریافت کنید.',
        'WAIT': 'لطفا صبر کنید...',
        'UNKNOWN_ERROR': '❌خطای ناشناخته!',
        'ENTER_SUBSCRIPTION_INFO': 'لطفا اطلاعات اشتراک خود را وارد کنید.\nیکی از کانفیگ ها، uuid یا لینک اشتراک⬇️',
        'SUBSCRIPTION_INFO_NOT_FOUND': '❌اطلاعات اشتراک یافت نشد!',
        'USER_NOT_FOUND': '❌کاربر یافت نشد.',
        'SUBSCRIPTION_UNLINKED': '✅اشتراک از ربات جداسازی شد',
        'USER_NAME': '👤نام:',
        'PLANS_LIST': '📋لیست پلن ها:',
        'PLANS_NOT_FOUND': '❌پلنی یافت نشد!',
        'PLAN_ADD_NAME': 'لطفا نام خود را وارد کنید:',
        'SUBSCRIPTION_SUCCESS_ADDED': '✅اشتراک شما با موفقیت اضافه شد.',
        'PLAN_INFO': '📋اطلاعات پلن انتخاب شده',
        'PLAN_INFO_SIZE': 'حجم پلن:',
        'PLAN_INFO_PRICE': 'قیمت پلن:',
        'PLAN_INFO_DAYS': 'زمان پلن:',
        'TOMAN': 'تومان',
        'REQUEST_SEND_SCREENSHOT': '⬇️لطفا رسید پرداخت خود را در زیر این پیام ارسال کنید:',
        'ERROR_TYPE_SEND_SCREENSHOT': '⬇️لطفا رسید پرداخت خود را به صورت عکس ارسال کنید:',
        'REQUEST_SEND_NAME': '⬇️لطفا نام خود را ارسال کنید:',
        'NO_SUBSCRIPTION': '❌شما هیچ اشتراکی ندارید!',
        'WAIT_FOR_ADMIN_CONFIRMATION': '✅اشتراک شما در انتظار تایید توسط ادمین است.\nلطفا صبر کنید.',
        'NEW_PAYMENT_RECEIVED': "پرداخت جدیدی ثبت شد",
        'PAYMENT_ASK_TO_CONFIRM': 'آیا شما این پرداخت را تایید میکنید؟',
        'REQUEST_SEND_TO_QR': 'لطفا کانفیگ یا لینک اشتراک خود را ارسال کنید:',
        'REQUEST_SEND_TO_QR_ERROR': 'متن ارسالی معتبر نیست\nلطفا کانفیگ یا لینک اشتراک خود را به صورت متنی ارسال کنید!',
        'USER_CONFIGS_LIST': '📋لیست کانفیگ های شما',
        'USER_CONFIGS_NOT_FOUND': '❌کانفیگی یافت نشد!',
        'ERROR_CONFIG_NOT_FOUND': '❌کانفیگ یافت نشد!',
        'ERROR_INVALID_COMMAND': '❌دستور نامعتبر!',
        'ALREADY_SUBSCRIBED': '❌اشتراک شما قبلا اضافه شده است.',
        'ERROR_INVALID_NUMBER': '❌لطفا مقداری عددی وارد کنید!',
        'CANCELED': '❌لغو شد',
        'SUBSCRIPTION_NOT_FOUND': '❌شما اشتراک فعالی ندارید!',
        'ZERO_BALANCE': '🔻موجودی کیف پول شما صفر می‌باشد',
        'WALLET_INFO_PART_1': '🔻موجودی کیف پول شما',
        'WALLET_INFO_PART_2': 'تومان می‌باشد',
        'INCREASE_WALLET_BALANCE_AMOUNT': '🔻لطفا مبلغی که قصد شارژ حساب خود دارید را به تومان وارد کنید',
        'MINIMUM_DEPOSIT_AMOUNT':'🔻لطفا مبلغ را به تومان و بیشتر از 30000 تومان وارد کنید',
        'LACK_OF_WALLET_BALANCE':'❌موجودی کیف پول شما کافی نیست\nلطفا از طریق دکمه [💰کیف پول] کیف پول خود را شارژ کنید',
        'ORDER_ID': 'شماره سفارش',
        'PAYMENT_CONFIRMED': '✅پرداخت شما تایید شد\n از طریق دکمه [📊وضعیت اشتراک] میتوانید به اطلاعات اشتراک خود دسترسی داشته باشید.',
        'ALREADY_RECEIVED_FREE': 'شما قبلا اکانت تست رایگان خود را دریافت نموده‌اید!',
        'GET_FREE_CONFIRMED' :  '✅اکانت تست رایگان شما با موفقیت ثبت شد\n از طریق دکمه [📊وضعیت اشتراک] میتوانید به اطلاعات اشتراک خود دسترسی داشته باشید.',
        'SUCCESSFUL_RENEWAL': '✅تمدید اشتراک شما با موفقیت انجام شد',
        'REQUEST_START': 'لطفا ربات را با دستور /start شروع کنید',
    }

}
MESSAGES = MESSAGES[LANG]
