import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];

const getItemById = (id) => {
  const search = listProducts.find(item => item.itemId === id);
  if (search) {
    return Object.fromEntries(Object.entries(search));
  };
};

const app = express();
const client = createClient();

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

const reserveStockById = (itemId, stock) => {
  return promisify(client.SET).bind(client)(`item.${itemId} ${stock}`)
};

const getCurrentReservedStockById = async (itemId) => {
  return promisify(client.GET).bind(client)(`item.${itemId}`);
};

app.get("/list_products/:itemId(\\d+)", (req, res) => {
  const id = Number.parseInt(req.params.itemId);
  const product = getItemById(Number.parseInt(id));

  if (!product) {
    res.json({status: "Product not found"});
    return;
  }

  getCurrentReservedStockById(id).then((ans) => Number.parseInt(ans || 0))
	.then((item) => {
	  productItem.currentQuantity = productItem.initialAvailableQuantity - item;
	  res.json(productItem);
	});
});

app.get("/reserve_product/:itemId(\\d+)", (req, res) => {
  const id = Number.parseInt(req.params.itemId);
  const product = getItemById(Number.parseInt(id));

  if (!product) {
    res.json({status: "Product not found"});
    return;
  }

  getCurrentReservedStockById(id).then((ans) => Number.parseInt(ans || 0))
	.then((stock) => {
	  if (stock) {
	    res.json({status: `Not enough stock available ${id}`});
	    return;
	  }
	  reserveStockById(id, stock + 1).then(() => {
	    res.json({status: `Reservation confirmed ${id}`});
	  });
	});
});

const resetProductsStock = () => {
  return Promise.all(
    listProducts.map(
      elem => promisify(client.SET).bind(client)(`elem.${elem.id} 0`)
    )
  );
};

app.listen(1245, () => {
  resetProductsStock().then(() => {
    console.log(`API available on localhost port 1245`);
  });
});

export default app;
