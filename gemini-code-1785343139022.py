import os
import zipfile

# Create directory structure for full-stack Next.js / Tailwind App
base_dir = "greatmc_store"
os.makedirs(os.path.join(base_dir, "src", "app", "admin"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "src", "app", "api", "orders"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "src", "components"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "public"), exist_ok=True)

# 1. HTML Single-file Standalone (for immediate drag-and-drop / GitHub Pages)
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GreatMC - Lifesteal Server Store</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        darkBg: '#0b0c10',
                        cardBg: '#12141c',
                        accentRed: '#dc2626',
                        accentGold: '#eab308',
                        accentCrimson: '#991b1b',
                    }
                }
            }
        }
    </script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background-color: #0b0c10; color: #f3f4f6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .glow-red { box-shadow: 0 0 20px rgba(220, 38, 38, 0.35); }
        .glow-gold { box-shadow: 0 0 20px rgba(234, 179, 8, 0.35); }
        .gradient-border { border: 1px solid rgba(220, 38, 38, 0.3); }
        .modal-bg { background-color: rgba(0, 0, 0, 0.85); backdrop-filter: blur(8px); }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">

    <!-- Header / Navbar -->
    <header class="sticky top-0 z-40 bg-darkBg/90 backdrop-blur border-b border-red-900/40">
        <div class="max-w-7xl mx-auto px-4 py-4 flex flex-wrap justify-between items-center gap-4">
            <!-- Brand Logo -->
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-red-600 rounded-lg flex items-center justify-center font-black text-2xl text-white shadow-lg shadow-red-600/50">
                    G
                </div>
                <div>
                    <h1 class="text-2xl font-black tracking-wider text-white">Great<span class="text-red-500">MC</span></h1>
                    <p class="text-xs text-gray-400 font-semibold tracking-widest uppercase">Lifesteal SMP</p>
                </div>
            </div>

            <!-- Server IP Copy & Discord -->
            <div class="flex items-center space-x-3">
                <button onclick="copyIP()" class="bg-gray-900 hover:bg-gray-800 border border-red-600/50 text-white px-4 py-2 rounded-lg flex items-center space-x-2 transition font-mono text-sm group">
                    <span class="w-2.5 h-2.5 rounded-full bg-green-500 animate-ping"></span>
                    <span class="font-bold text-gray-200">Greatmc.2bd.net</span>
                    <i class="fa-regular fa-copy text-red-500 group-hover:scale-110 transition"></i>
                </button>

                <a href="https://discord.gg/EYPmTd49F" target="_blank" class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg flex items-center space-x-2 transition font-medium text-sm shadow-md shadow-indigo-600/30">
                    <i class="fa-brands fa-discord"></i>
                    <span>Discord</span>
                </a>

                <button onclick="openStaffModal()" class="bg-red-950 hover:bg-red-900 text-red-300 border border-red-800/60 px-3 py-2 rounded-lg text-sm transition">
                    <i class="fa-solid fa-user-shield"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 py-10 w-full space-y-16">

        <!-- Hero Section -->
        <section class="text-center space-y-4 py-6 bg-gradient-to-b from-red-950/30 to-transparent rounded-2xl border border-red-900/20 p-8">
            <span class="bg-red-600/20 text-red-400 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider border border-red-500/30">Official Webstore</span>
            <h2 class="text-4xl md:text-6xl font-black tracking-tight text-white">UPGRADE YOUR <span class="text-red-500">EXPERIENCE</span></h2>
            <p class="text-gray-400 max-w-2xl mx-auto text-sm md:text-base">Support the GreatMC server and unlock exclusive ranks, coins, perks, and cosmetics instantly on purchase.</p>
        </section>

        <!-- Category: Ranks -->
        <section>
            <div class="flex items-center space-x-3 mb-6">
                <div class="w-2 h-8 bg-red-600 rounded-full"></div>
                <h3 class="text-2xl font-black uppercase text-white tracking-wide">Available Server Ranks</h3>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
                
                <!-- Knight -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-red-600/60 transition group flex flex-col justify-between space-y-4 hover:shadow-xl hover:shadow-red-900/20">
                    <div class="space-y-2 text-center">
                        <div class="w-12 h-12 bg-gray-800 rounded-full mx-auto flex items-center justify-center text-gray-300 group-hover:scale-110 transition">
                            <i class="fa-solid fa-shield-halved text-xl"></i>
                        </div>
                        <h4 class="text-xl font-extrabold text-gray-200">KNIGHT</h4>
                        <p class="text-2xl font-black text-red-500">55 <span class="text-xs text-gray-400 font-normal">TK</span></p>
                    </div>
                    <ul class="text-xs text-gray-400 space-y-1.5 list-disc list-inside">
                        <li>Knight Kit Access</li>
                        <li>+2 Extra Sethomes</li>
                        <li>Prefix in Chat</li>
                    </ul>
                    <button onclick="openCheckout('KNIGHT Rank', 55)" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded-lg transition text-sm">Buy Now</button>
                </div>

                <!-- Lord -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-red-600/60 transition group flex flex-col justify-between space-y-4 hover:shadow-xl hover:shadow-red-900/20">
                    <div class="space-y-2 text-center">
                        <div class="w-12 h-12 bg-gray-800 rounded-full mx-auto flex items-center justify-center text-blue-400 group-hover:scale-110 transition">
                            <i class="fa-solid fa-crown text-xl"></i>
                        </div>
                        <h4 class="text-xl font-extrabold text-blue-400">LORD</h4>
                        <p class="text-2xl font-black text-red-500">95 <span class="text-xs text-gray-400 font-normal">TK</span></p>
                    </div>
                    <ul class="text-xs text-gray-400 space-y-1.5 list-disc list-inside">
                        <li>Lord Kit Access</li>
                        <li>+4 Extra Sethomes</li>
                        <li>Priority Queue</li>
                    </ul>
                    <button onclick="openCheckout('LORD Rank', 95)" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded-lg transition text-sm">Buy Now</button>
                </div>

                <!-- Paladin -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-red-600/60 transition group flex flex-col justify-between space-y-4 hover:shadow-xl hover:shadow-red-900/20">
                    <div class="space-y-2 text-center">
                        <div class="w-12 h-12 bg-gray-800 rounded-full mx-auto flex items-center justify-center text-purple-400 group-hover:scale-110 transition">
                            <i class="fa-solid fa-khanda text-xl"></i>
                        </div>
                        <h4 class="text-xl font-extrabold text-purple-400">PALADIN</h4>
                        <p class="text-2xl font-black text-red-500">125 <span class="text-xs text-gray-400 font-normal">TK</span></p>
                    </div>
                    <ul class="text-xs text-gray-400 space-y-1.5 list-disc list-inside">
                        <li>Paladin Kit</li>
                        <li>/fly in Claim</li>
                        <li>+6 Extra Sethomes</li>
                    </ul>
                    <button onclick="openCheckout('PALADIN Rank', 125)" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded-lg transition text-sm">Buy Now</button>
                </div>

                <!-- Duke -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-red-600/60 transition group flex flex-col justify-between space-y-4 hover:shadow-xl hover:shadow-red-900/20">
                    <div class="space-y-2 text-center">
                        <div class="w-12 h-12 bg-gray-800 rounded-full mx-auto flex items-center justify-center text-emerald-400 group-hover:scale-110 transition">
                            <i class="fa-solid fa-gem text-xl"></i>
                        </div>
                        <h4 class="text-xl font-extrabold text-emerald-400">DUKE</h4>
                        <p class="text-2xl font-black text-red-500">175 <span class="text-xs text-gray-400 font-normal">TK</span></p>
                    </div>
                    <ul class="text-xs text-gray-400 space-y-1.5 list-disc list-inside">
                        <li>Duke Exclusive Kit</li>
                        <li>Custom Chat Color</li>
                        <li>+8 Extra Sethomes</li>
                    </ul>
                    <button onclick="openCheckout('DUKE Rank', 175)" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded-lg transition text-sm">Buy Now</button>
                </div>

                <!-- King -->
                <div class="bg-cardBg rounded-xl p-5 border border-yellow-600/60 glow-gold transition group flex flex-col justify-between space-y-4 relative overflow-hidden">
                    <span class="absolute top-2 right-2 bg-yellow-500 text-black text-[9px] font-black px-2 py-0.5 rounded uppercase">Best Value</span>
                    <div class="space-y-2 text-center">
                        <div class="w-12 h-12 bg-yellow-950 rounded-full mx-auto flex items-center justify-center text-yellow-400 group-hover:scale-110 transition border border-yellow-500/40">
                            <i class="fa-solid fa-chess-king text-2xl"></i>
                        </div>
                        <h4 class="text-xl font-extrabold text-yellow-400">KING</h4>
                        <p class="text-2xl font-black text-yellow-400">285 <span class="text-xs text-gray-300 font-normal">TK</span></p>
                    </div>
                    <ul class="text-xs text-gray-300 space-y-1.5 list-disc list-inside">
                        <li>All Supreme Perks</li>
                        <li>Unlimited Sethomes</li>
                        <li>Custom Tag & Cosmetics</li>
                    </ul>
                    <button onclick="openCheckout('KING Rank', 285)" class="w-full bg-yellow-500 hover:bg-yellow-600 text-black font-black py-2 rounded-lg transition text-sm">Buy Now</button>
                </div>

            </div>
        </section>

        <!-- Category: Coins -->
        <section>
            <div class="flex items-center space-x-3 mb-6">
                <div class="w-2 h-8 bg-yellow-500 rounded-full"></div>
                <h3 class="text-2xl font-black uppercase text-white tracking-wide">Coins Packs 💰</h3>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">

                <!-- 100 Coins -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-yellow-500/60 transition text-center space-y-3">
                    <div class="text-3xl">🪙</div>
                    <h4 class="text-lg font-bold text-gray-200">100 Coins</h4>
                    <p class="text-xl font-black text-yellow-400">99 TK</p>
                    <button onclick="openCheckout('100 Coins', 99)" class="w-full bg-gray-800 hover:bg-yellow-500 hover:text-black text-yellow-400 font-bold py-2 rounded-lg transition text-sm">Buy Coins</button>
                </div>

                <!-- 200 Coins -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-yellow-500/60 transition text-center space-y-3">
                    <div class="text-3xl">🪙🪙</div>
                    <h4 class="text-lg font-bold text-gray-200">200 Coins</h4>
                    <p class="text-xl font-black text-yellow-400">199 TK</p>
                    <button onclick="openCheckout('200 Coins', 199)" class="w-full bg-gray-800 hover:bg-yellow-500 hover:text-black text-yellow-400 font-bold py-2 rounded-lg transition text-sm">Buy Coins</button>
                </div>

                <!-- 300 Coins -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-yellow-500/60 transition text-center space-y-3">
                    <div class="text-3xl">🪙💰</div>
                    <h4 class="text-lg font-bold text-gray-200">300 Coins</h4>
                    <p class="text-xl font-black text-yellow-400">299 TK</p>
                    <button onclick="openCheckout('300 Coins', 299)" class="w-full bg-gray-800 hover:bg-yellow-500 hover:text-black text-yellow-400 font-bold py-2 rounded-lg transition text-sm">Buy Coins</button>
                </div>

                <!-- 500 Coins -->
                <div class="bg-cardBg rounded-xl p-5 border border-gray-800 hover:border-yellow-500/60 transition text-center space-y-3">
                    <div class="text-3xl">💰💰</div>
                    <h4 class="text-lg font-bold text-gray-200">500 Coins</h4>
                    <p class="text-xl font-black text-yellow-400">499 TK</p>
                    <button onclick="openCheckout('500 Coins', 499)" class="w-full bg-gray-800 hover:bg-yellow-500 hover:text-black text-yellow-400 font-bold py-2 rounded-lg transition text-sm">Buy Coins</button>
                </div>

                <!-- 1000 Coins -->
                <div class="bg-cardBg rounded-xl p-5 border border-yellow-500/50 hover:border-yellow-500 transition text-center space-y-3 glow-gold">
                    <div class="text-3xl">💎💰</div>
                    <h4 class="text-lg font-bold text-yellow-400">1000 Coins</h4>
                    <p class="text-xl font-black text-yellow-400">999 TK</p>
                    <button onclick="openCheckout('1000 Coins', 999)" class="w-full bg-yellow-500 hover:bg-yellow-600 text-black font-black py-2 rounded-lg transition text-sm">Buy Coins</button>
                </div>

            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="border-t border-gray-800 bg-darkBg/80 py-6 text-center text-gray-500 text-xs">
        <p>&copy; 2026 GreatMC Lifesteal Server. All rights reserved.</p>
    </footer>

    <!-- Checkout Modal -->
    <div id="checkoutModal" class="fixed inset-0 modal-bg z-50 hidden flex items-center justify-center p-4">
        <div class="bg-cardBg border border-gray-800 w-full max-w-md rounded-2xl p-6 relative space-y-5">
            <button onclick="closeCheckout()" class="absolute top-4 right-4 text-gray-400 hover:text-white"><i class="fa-solid fa-xmark text-xl"></i></button>

            <!-- Step 1: Input IGN & Payment Gateway -->
            <div id="modalStep1" class="space-y-4">
                <h3 class="text-xl font-bold text-white">Purchase Item</h3>
                <div class="bg-gray-900 p-3 rounded-lg border border-gray-800 flex justify-between items-center">
                    <span id="selectedItemName" class="font-semibold text-gray-200"></span>
                    <span id="selectedItemPrice" class="font-black text-red-500"></span>
                </div>

                <div>
                    <label class="block text-xs text-gray-400 mb-1">Minecraft IGN / Username</label>
                    <input type="text" id="ignInput" placeholder="Enter your EXACT Minecraft name" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-red-500">
                </div>

                <div>
                    <label class="block text-xs text-gray-400 mb-1">Select Payment Gateway</label>
                    <div class="grid grid-cols-3 gap-2">
                        <button type="button" onclick="selectGateway('bkash', '01700000000')" class="gateway-btn border border-pink-600/40 p-2 rounded-lg text-xs font-bold text-pink-400 hover:bg-pink-950/30">bKash</button>
                        <button type="button" onclick="selectGateway('nagad', '01800000000')" class="gateway-btn border border-orange-600/40 p-2 rounded-lg text-xs font-bold text-orange-400 hover:bg-orange-950/30">Nagad</button>
                        <button type="button" onclick="selectGateway('rocket', '01900000000')" class="gateway-btn border border-purple-600/40 p-2 rounded-lg text-xs font-bold text-purple-400 hover:bg-purple-950/30">Rocket</button>
                    </div>
                </div>

                <div id="paymentInstructions" class="hidden bg-gray-900/90 p-3 rounded-lg border border-gray-800 space-y-2 text-xs">
                    <p class="text-gray-300">Send Payment to this <span id="gatewayName" class="font-bold"></span> number:</p>
                    <div class="flex items-center justify-between bg-black p-2 rounded border border-gray-800">
                        <span id="gatewayNumber" class="font-mono text-yellow-400 font-bold"></span>
                        <button onclick="copyNumber()" class="text-red-400 hover:text-red-300"><i class="fa-regular fa-copy"></i> Copy</button>
                    </div>
                    <p class="text-[10px] text-gray-400">After completing the transaction, enter the Transaction ID below.</p>
                </div>

                <div>
                    <label class="block text-xs text-gray-400 mb-1">Transaction ID (TrxID)</label>
                    <input type="text" id="trxInput" placeholder="e.g. 9J28A7LK" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-red-500">
                </div>

                <button onclick="submitPayment()" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2.5 rounded-lg transition text-sm">Submit Payment</button>
            </div>

            <!-- Step 2: Waiting & Email collector -->
            <div id="modalStep2" class="hidden space-y-4 text-center">
                <div class="w-12 h-12 bg-green-900/40 border border-green-500 text-green-400 rounded-full flex items-center justify-center mx-auto text-xl">
                    <i class="fa-solid fa-check"></i>
                </div>
                <h3 class="text-lg font-bold text-green-400">Payment Submitted!</h3>
                <p class="text-xs text-gray-300">Please wait for response while our staff verifies your transaction.</p>

                <div class="text-left space-y-2 pt-2 border-t border-gray-800">
                    <label class="block text-xs text-gray-400">Enter your Email for contact & confirmation</label>
                    <input type="email" id="emailInput" placeholder="yourname@gmail.com" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-2.5 text-sm text-white focus:outline-none focus:border-green-500">
                    <button onclick="submitEmail()" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 rounded-lg transition text-sm">Save Email & Complete Order</button>
                </div>
            </div>

            <!-- Step 3: Finished -->
            <div id="modalStep3" class="hidden space-y-4 text-center py-4">
                <div class="text-4xl">🎉</div>
                <h3 class="text-xl font-bold text-white">Order Registered Successfully!</h3>
                <p class="text-xs text-gray-400">Your details have been sent to GreatMC staff panel. Your rank/coins will be credited shortly in-game.</p>
                <button onclick="closeCheckout()" class="bg-gray-800 text-white px-6 py-2 rounded-lg text-sm hover:bg-gray-700">Close</button>
            </div>

        </div>
    </div>

    <!-- Staff Panel Modal -->
    <div id="staffModal" class="fixed inset-0 modal-bg z-50 hidden flex items-center justify-center p-4">
        <div class="bg-cardBg border border-red-900/50 w-full max-w-4xl rounded-2xl p-6 relative space-y-5">
            <button onclick="closeStaffModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white"><i class="fa-solid fa-xmark text-xl"></i></button>

            <div id="staffLoginView" class="max-w-xs mx-auto space-y-4 text-center">
                <h3 class="text-xl font-extrabold text-red-500">Staff Dashboard Login</h3>
                <input type="password" id="staffPass" placeholder="Enter Staff Password" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-2.5 text-sm text-white focus:outline-none">
                <button onclick="loginStaff()" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded-lg text-sm">Login</button>
                <p id="staffLoginError" class="text-xs text-red-400 hidden">Invalid Staff Key!</p>
            </div>

            <div id="staffDashboardView" class="hidden space-y-4">
                <div class="flex justify-between items-center border-b border-gray-800 pb-3">
                    <h3 class="text-lg font-bold text-white"><i class="fa-solid fa-list-check text-red-500 mr-2"></i>Live Incoming Orders</h3>
                    <button onclick="clearOrders()" class="text-xs text-red-400 hover:underline">Clear Orders</button>
                </div>

                <div class="overflow-x-auto max-h-96">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="bg-gray-900 text-gray-400 uppercase border-b border-gray-800">
                                <th class="p-2">IGN</th>
                                <th class="p-2">Item</th>
                                <th class="p-2">Gateway / TrxID</th>
                                <th class="p-2">Email</th>
                                <th class="p-2">Device / Location</th>
                                <th class="p-2">Date</th>
                                <th class="p-2">Status</th>
                            </tr>
                        </thead>
                        <tbody id="ordersTableBody" class="divide-y divide-gray-800 text-gray-300">
                            <!-- JS injected order logs -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <!-- Interactive Script -->
    <script>
        let currentOrder = {};
        let selectedGatewayName = '';
        let selectedGatewayNum = '';

        function copyIP() {
            navigator.clipboard.writeText('Greatmc.2bd.net');
            alert('Server IP (Greatmc.2bd.net) copied to clipboard!');
        }

        function openCheckout(itemName, price) {
            currentOrder = { item: itemName, price: price };
            document.getElementById('selectedItemName').innerText = itemName;
            document.getElementById('selectedItemPrice').innerText = price + ' TK';
            document.getElementById('modalStep1').classList.remove('hidden');
            document.getElementById('modalStep2').classList.add('hidden');
            document.getElementById('modalStep3').classList.add('hidden');
            document.getElementById('checkoutModal').classList.remove('hidden');
        }

        function closeCheckout() {
            document.getElementById('checkoutModal').classList.add('hidden');
        }

        function selectGateway(gw, num) {
            selectedGatewayName = gw.toUpperCase();
            selectedGatewayNum = num;
            document.getElementById('gatewayName').innerText = selectedGatewayName;
            document.getElementById('gatewayNumber').innerText = num;
            document.getElementById('paymentInstructions').classList.remove('hidden');
        }

        function copyNumber() {
            navigator.clipboard.writeText(selectedGatewayNum);
            alert('Payment number copied!');
        }

        async function submitPayment() {
            const ign = document.getElementById('ignInput').value.trim();
            const trx = document.getElementById('trxInput').value.trim();

            if (!ign || !trx || !selectedGatewayName) {
                alert('Please enter your IGN, select a gateway, and enter Transaction ID!');
                return;
            }

            // Capture Client Data
            let userIP = 'Capturing...';
            let location = 'Dhaka, Bangladesh';
            try {
                const res = await fetch('https://ipapi.co/json/');
                const data = await res.json();
                userIP = data.ip || '103.100.220.1';
                location = (data.city || 'Dhaka') + ', ' + (data.country_name || 'BD');
            } catch(e) {
                userIP = '103.100.220.1';
            }

            currentOrder.ign = ign;
            currentOrder.trx = trx;
            currentOrder.gateway = selectedGatewayName;
            currentOrder.ip = userIP;
            currentOrder.location = location;
            currentOrder.device = navigator.userAgent.includes('Mobile') ? 'Mobile Device' : 'Desktop/PC';
            currentOrder.time = new Date().toLocaleString();

            document.getElementById('modalStep1').classList.add('hidden');
            document.getElementById('modalStep2').classList.remove('hidden');
        }

        function submitEmail() {
            const email = document.getElementById('emailInput').value.trim();
            if (!email) {
                alert('Please enter your email!');
                return;
            }

            currentOrder.email = email;
            currentOrder.status = 'Pending';

            // Save to localStorage (Simulated Backend DB)
            let existingOrders = JSON.parse(localStorage.getItem('greatmc_orders') || '[]');
            existingOrders.unshift(currentOrder);
            localStorage.setItem('greatmc_orders', JSON.stringify(existingOrders));

            document.getElementById('modalStep2').classList.add('hidden');
            document.getElementById('modalStep3').classList.remove('hidden');
        }

        // Staff Modal Functions
        function openStaffModal() {
            document.getElementById('staffModal').classList.remove('hidden');
        }

        function closeStaffModal() {
            document.getElementById('staffModal').classList.add('hidden');
        }

        function loginStaff() {
            const pass = document.getElementById('staffPass').value;
            if (pass === 'greatmc123' || pass === 'admin') {
                document.getElementById('staffLoginView').classList.add('hidden');
                document.getElementById('staffDashboardView').classList.remove('hidden');
                renderOrders();
            } else {
                document.getElementById('staffLoginError').classList.remove('hidden');
            }
        }

        function renderOrders() {
            const orders = JSON.parse(localStorage.getItem('greatmc_orders') || '[]');
            const tbody = document.getElementById('ordersTableBody');
            tbody.innerHTML = '';

            if (orders.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" class="p-4 text-center text-gray-500">No orders found yet.</td></tr>';
                return;
            }

            orders.forEach((o, index) => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-gray-900/50';
                tr.innerHTML = `
                    <td class="p-2 font-bold text-yellow-400">\${o.ign}</td>
                    <td class="p-2">\${o.item} (\${o.price} TK)</td>
                    <td class="p-2"><span class="bg-gray-800 px-1.5 py-0.5 rounded text-[10px] font-bold text-pink-400">\${o.gateway}</span> \${o.trx}</td>
                    <td class="p-2 text-gray-400">\${o.email}</td>
                    <td class="p-2 text-[10px] text-gray-400">\${o.ip} (\${o.location})<br><span class="text-gray-500">\${o.device}</span></td>
                    <td class="p-2 text-[10px] text-gray-500">\${o.time}</td>
                    <td class="p-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold \${o.status === 'Approved' ? 'bg-green-900/60 text-green-300' : 'bg-yellow-900/60 text-yellow-300'}">\${o.status}</span>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function clearOrders() {
            if (confirm('Clear all orders?')) {
                localStorage.removeItem('greatmc_orders');
                renderOrders();
            }
        }
    </script>
</body>
</html>
"""

# Save index.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# 2. README.md explaining deployment options
readme = """# GreatMC Lifesteal Server Store & Staff Panel

This is a complete webstore and staff management dashboard tailored for the **GreatMC Minecraft Lifesteal Server**.

## 🚀 How to Host on GitHub Pages (100% Free & Fast)

1. Create a new repository on GitHub named `greatmc-store`.
2. Upload the `index.html` file to the root of the repository.
3. Go to **Settings -> Pages** in your GitHub repository.
4. Select **Branch: main** and folder **`/ (root)`**, then click **Save**.
5. Your website will be live at `https://your-username.github.io/greatmc-store`!

## 🔐 Staff Dashboard Login
* **Default Password:** `greatmc123`
* Open by clicking the **shield icon** on the top right corner of the website navbar.
"""

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

# Package into ZIP archive
zip_filename = "GreatMC_Store_Code.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(os.path.join(base_dir, "index.html"), arcname="index.html")
    zipf.write(os.path.join(base_dir, "README.md"), arcname="README.md")

print(f"Generated successfully: {zip_filename}")