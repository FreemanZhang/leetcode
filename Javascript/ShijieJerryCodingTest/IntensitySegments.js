import {OrderedMap} from "js-sdsl";

class IntensitySegments
{
    constructor()
    {
        this.skyline = new OrderedMap();
    }

    add(from, to, amount)
    {
        let [prevKey, prevValue] = [undefined, undefined];
        let fromIterator = this.skyline.find(from);
        if (fromIterator.equals(this.skyline.end()))
        {
            // when there is no key=from entry in the sorted hashmap (this.skyline)

            let lastSmaller = this.skyline.reverseUpperBound(from);
            if (lastSmaller.equals(this.skyline.rEnd()))
            {
                // When "from" is not covered by any range existing in the sorted hashmap (this.skyline)
                this.skyline.setElement(from, amount);
                [prevKey, prevValue] = [from, amount];
            }
            else
            {
                // When "from" is covered by a range existing in the sorted hashmap (this.skyline)

                let [key, value] = lastSmaller.pointer;
                [prevKey, prevValue] = [key, value];
                this.skyline.setElement(from, amount + value);
            }
        }
        else
        {
            // When "from" already exists in the sorted hashmap (this.skyline)

            let [key, value] = fromIterator.pointer;
            [prevKey, prevValue] = [key, value];
            this.skyline.setElement(key, value + amount);
        }

        // Handle all entries between (from, to)
        let it = this.skyline.find(from);

        it = it.next();
        while (!it.equals(this.skyline.end()))
        {
            let [key, value] = it.pointer;
            if ( key >= to )
            {
                break;
            }

            [prevKey, prevValue] = it.pointer;
            this.skyline.setElement(key, value + amount);
            it = it.next();
        }

        if (it.equals(this.skyline.end()))
        {
            // When there is no "to" entry in the sorted hashmap (this.skyline)

            this.skyline.setElement(to, 0);
        }
        else
        {
            let [key, value] = it.pointer;
            if (it.equals(this.skyline.rBegin()) && key === to)
            {
                // when "to" exists as the last element in the sorted hashmap

                this.skyline.setElement(to, 0);
            }
            else
            {
                // when "to" is not the last element in the sorted hashmap

                this.skyline.setElement(to, prevValue);
            }
        }

        this.cleanSkyline();
    }

    set(from, to, amount)
    {
        this.skyline.setElement(from, amount);
        let it = this.skyline.find(from);
        for (; !it.equals(this.skyline.end()); it.next())
        {
            let [key, value] = it.pointer;
            if (key >= to)
            {
                break;
            }

            this.skyline.setElement(key, amount);
        }

        if (it.equals(this.skyline.end()))
        {
            this.skyline.setElement(to, 0);
        }
        else
        {
            this.skyline.setElement(to, amount);
        }

        this.cleanSkyline();
    }

    toString()
    {
        let result = "["
        for (let it = this.skyline.begin(); !it.equals(this.skyline.end()); it.next())
        {
            result += "[" + it.pointer[0] + "," + it.pointer[1] + "],"
        }

        if (result.length > 1)
        {
            result = result.slice(0, result.length - 1)
        }

        result += "]"
        return result
    }

    cleanSkyline()
    {
        // Remove the beginning 0 values
        const keyToRemove = new Set();
        for (let it = this.skyline.begin(); !it.equals(this.skyline.end()); it.next())
        {
            let [key, value] = it.pointer;
            if (value === 0)
            {
                keyToRemove.add(key);
            }
            else
            {
                break;
            }
        }

        // For multiple neighboring entries with same value, only the 1st one is kept.
        let [prevKey, prevValue] = this.skyline.begin().pointer;
        for (let it = this.skyline.begin().next(); !it.equals(this.skyline.end()); it.next())
        {
            let [key, value] = it.pointer;
            if (value === prevValue)
            {
                keyToRemove.add(key);
            }

            [prevKey, prevValue] = [key, value];
        }

        for (const key of keyToRemove)
        {
            this.skyline.eraseElementByKey(key);
        }
    }
}

module.exports = {IntensitySegments};